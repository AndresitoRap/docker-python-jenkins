FROM python:3

COPY . /app
WORKDIR /app
COPY . .
CMD [ "python", "index.py" ]