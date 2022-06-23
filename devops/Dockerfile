FROM python:3.8-alpine
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apk update
RUN apk add curl docker git docker-compose
RUN curl -L https://github.com/docker/compose/releases/download/1.25.0/docker-compose -o /usr/local/bin/docker-compose 
RUN mkdir /test && cd /test && git clone -b weight --single-branch https://github.com/yairelmaliah/gan-shmuel-team-a.git
WORKDIR /app
COPY . .
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]