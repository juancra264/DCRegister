from os import environ
from datetime import timedelta
import os


# Base config for APP and Extension
class Config(object):
    # DO NOT use Unsecure Secrets in production environments
    # Generate a safe one with:
    #    python -c "import os; print(repr(os.urandom(24)));"
    SECRET_KEY = 'ymuQvbaQnztPnwTP7Fvwc85NDKSGzK2NDX97UHQDyRMXaqS5'
    COOKIE_SECURE = 'Secure'
    COOKIE_DURATION = timedelta(days=365)
    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids a SQLAlchemy Warning
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'app/translations/')
    BABEL_DEFAULT_LOCALE = 'es'
    # Flask-Mail settings
    # For smtp.gmail.com to work, you MUST set "Allow less secure apps"
    # to ON in Google Accounts.
    # Change it in https://myaccount.google.com/security#connectedapps
    # (near the bottom).
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'juancra264@gmail.com'
    MAIL_PASSWORD = '12345'
    MAIL_DEFAULT_SENDER = '"DC Register" <juancra264@gmail.com>'
    ADMINS = [
        '"Admin One" <admin1@gmail.com>',
    ]


class ProductionConfig(Config):
    DEBUG = False
    # Security
    #SESSION_COOKIE_HTTPONLY = True
    #REMEMBER_COOKIE_HTTPONLY = True
    #REMEMBER_COOKIE_DURATION = 3600
    # PostgreSQL database
    #SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
    #    environ.get('DATABASE_USER', 'dcregister'),
    #    environ.get('DATABASE_PASSWORD', 'DCregister2020'),
    #    environ.get('DATABASE_HOST', '127.0.0.1'),
    #    environ.get('DATABASE_PORT', 5432),
    #    environ.get('DATABASE_NAME', 'dcregister')
    #)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgresql://{}:{}@{}:{}/{}'.format(
                                                 'dcregister',
                                                 'DCregister2020',
                                                 '127.0.0.1',
                                                 5432,
                                                 'dcregister'))


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../app.sqlite"


config_dict = {
    'Production': ProductionConfig,
    'Development': DevelopmentConfig
}
