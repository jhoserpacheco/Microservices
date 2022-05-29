FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /entrance-service
COPY requirements.txt /entrance-service/
RUN pip install -r requirements.txt
COPY . /entrance-service/
RUN python manage.py migrate