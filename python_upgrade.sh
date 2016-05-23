sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install gunicorn
pip install django
# gunicorn ask.wsgi:application --bind 0.0.0.0:8000

sudo apt-get update
sudo apt-get install python-dev libmysqlclient-dev
sudo apt-get install python3-dev
pip install mysqlclient
