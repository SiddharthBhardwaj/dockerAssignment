# start by pulling the python image
FROM keinos/sqlite3:latest
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /root/dockerImage/requirements.txt

# switch working directory
WORKDIR /root/dockerImage

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# copy every content from the local file to the image
COPY . /root/dockerImage

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
