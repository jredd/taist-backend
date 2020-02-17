FROM python:3.8

RUN mkdir /taist_app
WORKDIR /taist_app

ADD . /taist_app/
RUN pip install -r requirements.txt

CMD ['gunicorn', 'app.wsgi:application', '—-bind=0.0.0.0:8000', '—-workers=3']
