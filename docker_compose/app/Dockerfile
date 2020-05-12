FROM python:3.7-slim

# VOLUME MAPPED ./web:/var/www/app
WORKDIR /var/www/app
ADD ./web .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# start the uWSGI
CMD ["uwsgi", "app.ini"]