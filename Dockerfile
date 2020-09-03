FROM python:3.7-stretch AS Notes
LABEL stage="beta"

# installation external system libraries
RUN apt -y update

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
