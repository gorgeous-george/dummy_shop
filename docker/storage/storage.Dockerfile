FROM python:3.9

COPY microservice_storage/requirements.txt /

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY ./docker/storage/docker-entrypoint.sh ./docker/storage/wait-for-command.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh

COPY /microservice_storage/ /app

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]