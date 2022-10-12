FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
COPY . .
RUN set FLASK_APP=app
EXPOSE 8080
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]