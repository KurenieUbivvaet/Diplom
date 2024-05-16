FROM python:3.12.1-slim-bullseye

RUN mkdir -p ./Diplom
WORKDIR ./Diplom

COPY . . 

RUN pip install Django django-filter djangorestframework pillow uuid psycopg2 requests 

CMD python manage.py runserver