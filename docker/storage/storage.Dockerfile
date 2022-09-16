FROM python:3.9

COPY /microservice_storage/requirements.txt /

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY /microservice_storage/ /app

WORKDIR /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]