FROM python:3.10.0b1-alpine3.12

RUN apk --update --no-cache add libffi-dev gcc musl-dev make libevent-dev build-base
RUN apk add bash

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "./api.py"]
