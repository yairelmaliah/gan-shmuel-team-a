FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /src/requirements.txt

# switch working directory
WORKDIR /src

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .

WORKDIR /src/app/
# configure the container to run in an executed manner
ENTRYPOINT [ "python3", "app.py" ]
# ENTRYPOINT ["tail", "-f", "/dev/null"]
