FROM python:3.8.10
COPY requirements.txt /zoughts/
WORKDIR /zoughts/
RUN pip install -r requirements.txt
COPY . /zoughts/
CMD [ "./docker/app/startup.sh" ]