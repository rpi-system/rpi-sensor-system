# Verwende das Python Slim Image
FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app.py /app/app.py
RUN chmod +x /app/app.py

CMD ["python", "/app/app.py"]