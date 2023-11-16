#Creacion de imagen base
FROM python:3.8

WORKDIR /app

COPY requirements.txt  /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "python", "main.py" ]