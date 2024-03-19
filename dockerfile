FROM python:3

WORKDIR /app

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
