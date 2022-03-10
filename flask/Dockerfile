FROM python:alpine3.14

WORKDIR /usr/src/myproject
COPY app.py .

EXPOSE 5000

RUN export FLASK_APP=app && pip install Flask && pip install redis 

CMD ["flask", "run", "--host=0.0.0.0"]