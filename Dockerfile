FROM python:3.10-slim

# Copy local code to the container

WORKDIR .
COPY . ./

EXPOSE 8080

# Install production dependencies.
RUN pip install --no-cache-dir -r src/requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
#CMD ["uvicorn", "src.main:app", "--port", "8080"]
CMD ["fastapi", "run", "src/main.py", "--port", "8080"]
