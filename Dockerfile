# - 1. Specifying our base image
FROM python:3.8

# - 2. Set the working directory in the container
WORKDIR /usr/src/app/PlotPoints

# - 3. Add the files that make up the Application
#
# - 3.a. Install all Python requirements for our app to run
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#
# - 3.b Copy the python files and the folder into our image
COPY utilities/ ./utilities/
COPY info_inputFile.json .
COPY mainRun.py .

# - 4. Command for running the application 
CMD ["python", "mainRun.py"]

