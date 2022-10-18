# pull the official base image
FROM python:3.10.8-buster

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip3 install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 80

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]