FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]