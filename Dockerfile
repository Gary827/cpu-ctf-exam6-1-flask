FROM python:3.7.2-stretch

WORKDIR /app

COPY ./app/ /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5001

CMD python httpprac.py