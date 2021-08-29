# pull official base image
FROM python:3.8.2

# set work directory
WORKDIR /usr/src/zoughts

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install gcc python3-dev musl-dev -y

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# CMD [ "./docker/db-init/wait-for-postgres.sh", "db", "./docker/db-init/startup.sh" ]