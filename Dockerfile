# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the Scores.txt file to the desired location inside the container
COPY Scores.txt /Scores.txt

# Make port 80 available to the world outside this container
EXPOSE 8777

# Define environment variable
#ENV NAME World

# Command to run the Flask app from main_game
CMD ["python", "main_game.py"]
