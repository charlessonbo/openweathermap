# Weather app
web based application get weather by location

Technology used:
- Django framework
- API integration openweathermap.org
- leaflet for location map



## INITIAL SETUP


running this command in terminal to create a virtual environment.
```bash
python -m venv venv
```

to go into your virtual environment
 ```bash
 venv/bin/activate
```

to install Django packages
 ```bash
pip install -r requirements.txt
```

to setup database
 ```bash
python manage.py migrate
```

to run web application 
 ```bash
python manage.py runserver
```

## NOTE
Creating location data for location list page

create user by running command in terminal python manage.py createsuperuser

add location in admin page (http://127.0.0.1:8000/admin)
