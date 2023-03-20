# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install uvicorn
# Copy the rest of the application code into the container
COPY . .

# Expose the port that the application will listen on
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
