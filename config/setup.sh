#!/bin/bash -x

# Install Python programs (Flask, UWSGI)
pip install --upgrade pip
pip install -r /usr/local/etc/requirements.txt

# Add our Nginx config
ln -s /usr/local/etc/nginx.conf /etc/nginx/conf.d/ 
mkdir /etc/service/nginx
cp /usr/local/etc/nginx.sh /etc/service/nginx/run
chmod +x /etc/service/nginx/run

# Add our uWSGI config
mkdir /etc/uwsgi 
mkdir /etc/uwsgi/vassals 
ln -s /usr/local/etc/uwsgi.ini /etc/uwsgi/vassals/
mkdir /etc/service/uwsgi
cp /usr/local/etc/uwsgi.sh /etc/service/uwsgi/run
chmod +x /etc/service/uwsgi/run

# Add missing directories, set permissions
mkdir /var/run/www
chown -R www-data:www-data /var/run/www
mkdir /var/log/uwsgi
chown -R www-data:www-data /var/log/uwsgi
