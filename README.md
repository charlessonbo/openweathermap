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

 To go into your virtual environment
 ```bash
 venv/bin/activate
```

-To install depedency pip install -r requirements.txt

-To setup database python manage.py migrate

-to run web application python manage.py runserver


NOTE
-creating data for location list page
create user by running command in terminal python manage.py createsuperuser
add location in admin page http://127.0.0.1:8000/admin
