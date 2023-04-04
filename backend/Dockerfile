#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="Siddharth.Bhardwaj"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /root/dockerAssignment/backend

#to COPY the remote file at working directory in container
COPY app.py ./
# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "app.py"]
