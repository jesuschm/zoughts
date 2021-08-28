FROM python:3.8.10
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt /zoughts/
WORKDIR /zoughts/
RUN pip install -r requirements.txt
COPY . /zoughts/
CMD [ "./docker/db-init/wait-for-postgres.sh", "db", "./docker/db-init/startup.sh" ]
