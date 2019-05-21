# basic flask application

see `TestFlask.postman_collection.json` what's possible


but basically just an REST API running
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```

exposing these routes:
- `/` renders `home.html`
- `/<str:name>` renders  `home.html`

and more important:
- `/user/<string:name>` 
  - GET
  - POST
  - PUT
  - DELETE
- `/users/`
  - DELETE



hints for the `Dockerfile`:
inspired by steal with pride:
- https://runnable.com/docker/python/dockerize-your-flask-application
- http://containertutorials.com/docker-compose/flask-simple-app.html


## version 1
```
FROM python:3.6-alpine

COPY ./ ./app
WORKDIR ./app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
```

## alternative 1 :-)
```
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
```

