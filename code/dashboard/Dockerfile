FROM ubuntu
RUN apt-get upgrade && apt-get update
RUN apt install -y python3 python3-pip
WORKDIR /code/
COPY . /code/
RUN pip install -r requirements.txt
CMD ["python", "app.py"]