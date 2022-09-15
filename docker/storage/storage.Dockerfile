FROM python:3.9

COPY ./storage/requirements.txt /

RUN pip install -r requirements.txt

COPY ./storage/ /app

WORKDIR /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]