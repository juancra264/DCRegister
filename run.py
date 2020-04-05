from os import environ
from sys import exit
from config import config_dict
from app import create_app


get_config_mode = environ.get('CONFIG_MODE', 'Production')
try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid CONFIG_MODE environment variable entry.')


# Setup Flask-Script with command line commands
app = create_app(config_mode)
