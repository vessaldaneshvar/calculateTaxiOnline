FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
COPY . /code/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" , "app.py" ]
