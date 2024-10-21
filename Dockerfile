# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /home/data

# Copy the text files to the container
COPY IF.txt /home/data/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

# Copy the Python script (named 'code.py')
COPY code.py /home/data/code.py

# Install any required dependencies (optional, if any)
# RUN pip install --no-cache-dir -r /home/data/requirements.txt

# Command to run the Python script
CMD ["python", "/home/data/code.py"]
