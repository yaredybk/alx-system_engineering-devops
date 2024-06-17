#!/usr/bin/env bash
#install certbot to enable https with nginx

sudo snap install --classic certbot

sudo ln -s /snap/bin/certbot /usr/bin/certbot

sudo certbot --nginx
#or run this
#sudo certbot certonly --nginx

sudo certbot renew --dry-run

