# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
RUN mkdir /app
WORKDIR /app

# Copy the Flask app files and the trained model pickle file to the container
COPY . .

# Install Flask and any other dependencies you might have
RUN pip install -r requirements.txt

# Expose the port your Flask app will run on (usually 5000)
EXPOSE 5000

ENV FLASK_APP=BHP/server/server.py
# Command to run your Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
