FROM python:3.8.2-alpine
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
CMD ["python","app.py"]