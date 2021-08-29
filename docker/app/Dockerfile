FROM python:3.7.1
COPY requirements.txt /zoughts/
WORKDIR /zoughts/
RUN pip install -r requirements.txt
COPY . /zoughts/
CMD [ "./docker/app/startup.sh" ]