FROM python:3.8-slim
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["python", "app.py"]
