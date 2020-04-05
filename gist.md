# Python Heroku Deployment
> Steps to create a postgres database and deply a Python app to Heroku

### Install gunicorn locally
```
pipenv install gunicorn
or
pip install gunicorn
```

### Install Heroku CLI
https://devcenter.heroku.com/articles/heroku-cli


### Verifying your installation
```
heroku --version
```

### Login via CLI
```
heroku login -i
```

### Create app
```
heroku create appname
```

### Create database
```
heroku addons:create heroku-postgresql:hobby-dev --app appname
```

### Get URI
```
heroku config --app appname

# Add to your app
```

### Create Procfile
```
touch Procfile

# Add this
web: gunicorn app:app
```

### Create requirements.txt
```
pip freeze > requirements.txt
```

### Create runtime.txt
```
touch runtime.txt

# Add this
python-3.7.6
```
### Deploy with Git
```
git init
git add . && git commit -m 'Deploy'
heroku git:remote -a appname
git push heroku master
```

### Add table to remote database
```
heroku run python
>>> from app import db
>>> db.create_all()
>>>exit()
```

### Visit app
```
heroku open
```