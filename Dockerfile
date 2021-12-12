FROM python:3.9
# Setting PYTHONUNBUFFERED to a non empty value ensures that
#    the python output is sent straight to terminal
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000