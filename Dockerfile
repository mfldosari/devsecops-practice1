FROM python:3.10-slim

# workdir is the directory where the command will be run
# and where the files will be copied to
WORKDIR /app
# Copy the requirements file to the container
# and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the rest of the files to the container
# This includes the app.py file
COPY . .
# Expose the port that the app will run on 5000
EXPOSE 5000
#run the app
# CMD is the command that will be run when the container is started
# The command is run in the context of the WORKDIR
CMD ["python", "simple_app.py"]
