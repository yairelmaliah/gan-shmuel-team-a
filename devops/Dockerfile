FROM python:3.8-alpine
WORKDIR /app
COPY ./requirements.txt .
RUN apk get update \
    && apk add --no-cache git \
    && apk add --no-cache docker \
    && apk add docker-compose 
RUN pip install -r requirements.txt
RUN pip install requests
WORKDIR /app
COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]