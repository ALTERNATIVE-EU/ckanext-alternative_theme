# ckanext-alternative_theme

CKAN extension that changes the default theme of the platform to match the look of ALTERNATIVE.

## Setup

1. Install <a href="https://docs.ckan.org/en/2.9/extensions/tutorial.html#installing-ckan" target="_blank">CKAN</a>

2. Clone the repository in the `src` dir (usually located in `/usr/lib/ckan/default/src`)
    ```
    cd /usr/lib/ckan/default/src
    git clone https://github.com/ALTERNATIVE-EU/ckanext-alternative_theme.git
    ```

3. Build the extension
    ```
    . /usr/lib/ckan/default/bin/activate
    cd /usr/lib/ckan/default/src/ckanext-alternative_theme
    sudo python3 setup.py develop
    ```

4. Add the extension to your list of plugins in the ckan config file (usually `/etc/ckan/default/ckan.ini`)
   ```
   ckan.plugins = stats text_view recline_view ckanext-alternative_theme
   ```

5. Start CKAN
   ```
   . /usr/lib/ckan/default/bin/activate
   sudo ckan -c /etc/ckan/default/ckan.ini run
   ```
