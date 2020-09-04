FROM python:3.7-stretch AS Notes
LABEL stage="beta"

# installation external system libraries
ADD wkhtmltox_0.12.6-1.stretch_amd64.deb /tmp/w.deb
RUN apt -y update && dpkg -i /tmp/w.deb; apt-get -f install -y; rm -rf /var/lib/apt/lists/*

# copy our application code
WORKDIR /app
ADD ./requirements.txt ./requirements.txt

# fetch app specific deps
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
ADD ./source .

VOLUME /app/static
VOLUME /app/logs

RUN python manage.py collectstatic --no-input && python manage.py migrate

EXPOSE 8000

RUN chown www-data:www-data -R .
ENTRYPOINT ["uwsgi", "--master", "--enable-threads", "--emperor", "/app/uwsgi/config.ini"]
