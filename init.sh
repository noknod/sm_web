#echo $PATH

sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf.hello.py /etc/gunicorn.d/conf.hello.py
sudo gunicorn -c /etc/gunicorn.d/conf.hello.py hello:app
#sudo /etc/init.d/gunicorn restart

sudo ln -sf /home/box/web/etc/gunicorn.conf.py /etc/gunicorn.d/conf.py
#sudo gunicorn -c /etc/gunicorn.d/conf.py ask.wsgi:application
source venv/bin/activate
gunicorn -c /etc/gunicorn.d/conf.py ask.wsgi:application
