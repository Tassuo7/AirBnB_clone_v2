#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

apt update -y
apt install -y nginx

mkdir -p data/web_static/releases/test
mkdir -p data/web_static/shared

echo "<html>
  <head>
  </head>
  <body>
    fake html!
  </body>
</html>" | tee data/web_static/releases/test/index.html

ln -sf data/web_static/releases/test data/web_static/current

chown -R ubuntu:ubuntu data/

sudo sed -i "/server_name _;/a \\\tlocation /hbnb_static/ {\n\t\talias data/web_static/current/;\n\t}\n" etc/nginx/sites-available/default

sudo service nginx restart
