from sys import exit
from os import environ
from config import config_dict
from app import create_app


get_config_mode = 'Production'
try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid CONFIG_MODE environment variable entry.')


# Setup Flask-Script with command line commands
app = create_app(config_mode)
