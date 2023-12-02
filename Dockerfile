# Use an official Python runtime as a base image
FROM --platform=linux/amd64 python:3.10

# Set the working directory in the container
WORKDIR /app

COPY ./requirements.txt  /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8980

COPY . .

# 定义启动应用程序的命令
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
