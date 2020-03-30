# DCRegister - Web App
> Python Flask & Extensions


# Configuring SMTP

Edit the `local_settings.py` file.

Specifically set all the MAIL_... settings to match your SMTP settings

Note that Google's SMTP server requires the configuration of "less secure apps".
See https://support.google.com/accounts/answer/6010255?hl=en

Note that Yahoo's SMTP server requires the configuration of "Allow apps that use less secure sign in".
See https://help.yahoo.com/kb/SLN27791.html


## Quick Start

```bash
# Install dependencies
pipenv shell
pipenv install
# Create DB tables and populate the roles and users tables
pipenv run python manage.py init_db

# Start the Flask development web server
pipenv run python manage.py runserver

# Start the server for production
# Serve on localhost:5000
pipenv run gunicorn --config gunicorn.py wsgi:app
```

## Get the python libraries:

```bash
# Export the python libraries:
pipenv lock --requirements > requirements.txt
```
