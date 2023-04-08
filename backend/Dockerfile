# start by pulling the python image
FROM python:3.8-alpine
FROM keinos/sqlite3:latest


# run a command to change the folder permissions
RUN chmod -R 777 /root/dockerAssignment
RUN docker run --rm -it -v "$(pwd):/workspace" -w /workspace keinos/sqlite3

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
