#!/usr/bin/env bash
# Install nginx web server
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow http
# Create the folders
# mkdir -p (if file exists)
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# create the fake index
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html
# create the simbolyc link
ln -sf /data/web_static/releases/test/ /data/web_static/current
# ownership of the /data/ folder to the ubuntu user AND group
# chown: change owner, chgrp: change group
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
# add the configuration default in nginx (alias)
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
    add_header X-Served-By $HOSTNAME;
    location /hbnb_static {
        alias /data/web_static/current;
    }
}" > /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
