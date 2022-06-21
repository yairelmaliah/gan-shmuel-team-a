FROM python:alpine3.16
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
