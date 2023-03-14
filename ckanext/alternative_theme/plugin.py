# encoding: utf-8

'''plugin.py

'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.authz as authz
import ckan.model as model


def user_list(context, data_dict=None):
    user = model.User.get(context['user'])

    if authz.is_sysadmin(user.name):
        return {'success': True}
    else:
        return {'success': False, 'msg': 'Only system administrators can see users'}


class AlternativeThemePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):

        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        # 'templates' is the path to the templates dir, relative to this
        # plugin.py file.
        toolkit.add_template_directory(config, 'templates')

        # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'public')

    plugins.implements(plugins.IAuthFunctions)

    def get_auth_functions(self):
        return {'user_list': user_list}
