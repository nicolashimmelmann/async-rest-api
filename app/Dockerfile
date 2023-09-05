FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

CMD ["python3", "main.py"]
