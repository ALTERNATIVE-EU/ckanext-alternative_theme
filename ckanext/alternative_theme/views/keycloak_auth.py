import logging
import copy
import string
import secrets

from flask import Blueprint
from six import text_type

import ckan.plugins.toolkit as toolkit
import ckan.model as model
import ckan.authz as authz
from ckan.lib import base
from ckan.views.user import set_repoze_user
from ckan.common import config, g, request


log = logging.getLogger(__name__)
keycloak_auth = Blueprint(u'keycloak_auth', __name__)


def keycloak_change_password():
    u'''Redirects the user to keycloak identity provider for password change
    '''
    server_url = config.get('ckanext.keycloak.server_url')
    realm = config.get('ckanext.keycloak.realm')
    frontend_client_id = config.get('ckanext.keycloak.frontend_client_id')

    redirect_url = (
        server_url
        + "/realms/"
        + realm
        + "/login-actions/reset-credentials"
        + "?client_id="
        + frontend_client_id
    )

    return toolkit.redirect_to(redirect_url)

def jupyterhub_login():
    u'''Redirects the user to jupyterhub
    '''
    ckan_url = config.get('ckanext.keycloak.ckan_url')
    parsed_url = urlparse(ckan_url)
    host = parsed_url.netloc.split(':')[0]
    jupyterhub_host = 'jupyterhub.' + host[(len(host.split('.')[0]) + 1):]

    redirect_url = (
        "https://"
        + jupyterhub_host
        + "/"
    )

    return toolkit.redirect_to(redirect_url)

auth_endpoint = config.get('ckanext.keycloak_auth.auth_endpoint', '/authenticate')
keycloak_auth.add_url_rule(auth_endpoint, view_func=auth, methods=[u'GET', u'POST'])
keycloak_auth.add_url_rule(u'/user/keycloak_login', view_func=keycloak_login)
keycloak_auth.add_url_rule(u'/user/jupyterhub_login', view_func=jupyterhub_login)
keycloak_auth.add_url_rule(u'/user/keycloak_change_password', view_func=keycloak_change_password)