# Restaurants
Create new enviroment using pipenv, venv etc.\
Clone this repository\
Install all requirements using ```pip install -r requirements.txt```\
Then run
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
You should see app working on `127.0.0.1:8000`\
Go to `127.0.0.1:8000/admin` to create users
