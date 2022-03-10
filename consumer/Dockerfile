FROM python:alpine3.14

WORKDIR /usr/src/myproject
COPY  consumer.py .


RUN pip install psycopg2-binary && pip install redis

CMD ["python", "consumer.py"]