FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

#CMD python manage.py makemigrations
#CMD python manage.py  migrate

#CMD gunicorn --workers=1 --bind 0.0.0.0:80 djecommerce.wsgi
CMD python manage.py runserver 0:80