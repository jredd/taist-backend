FROM python:3.8

RUN mkdir /taist_app
WORKDIR /taist_app

ADD . /taist_app/
RUN pip install -r app/requirements.txt

CMD ['gunicorn', 'app.wsgi:application', '—-bind=0.0.0.0:8000', '—-workers=3']


#FROM nginx
#
#RUN rm /etc/nginx/conf.d/default.conf
#COPY django.conf /etc/nginx/conf.d
