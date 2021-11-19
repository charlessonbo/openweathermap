# Weather app
web based application get weather by location

Technology used:
- Django framework
- API integration openweathermap.org
- leaflet for location map\\\




INITIAL SETUP

 running this command in terminal
 
-Create a virtual environment python -m venv venv

-To go into your virtual environment: venv/bin/activate

-To install depedency pip install -r requirements.txt

-database setup python manage.py migrate

-to run web application python manage.py runserver


NOTE
-creating data for location list page
create user by running command in terminal python manage.py createsuperuser
add location in admin http://127.0.0.1:8000/admin
