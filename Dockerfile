FROM python:3.6.2-slim

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "./manage.py", "runserver", "--host", "0.0.0.0", "--port", "8080" ]
