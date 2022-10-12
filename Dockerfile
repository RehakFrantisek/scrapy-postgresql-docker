FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
COPY . .
CMD set FLASK_APP=app
CMD flask run