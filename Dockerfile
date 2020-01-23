FROM python:3.6.8

RUN mkdir /zpx
WORKDIR /zpx
ADD . /zpx/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/zpx/run.py"]