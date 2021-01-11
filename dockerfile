FROM python:3.6.10-slim-stretch
WORKDIR /app
ADD . /app
RUN cd api && pip install -r requirements.txt
WORKDIR /app/api

CMD [ "gunicorn", "-c", "gunicorn.conf.py", "wsgi:create_app()" ]
