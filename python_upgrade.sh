sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install gunicorn
pip install django
# gunicorn ask.wsgi:application --bind 0.0.0.0:8000
