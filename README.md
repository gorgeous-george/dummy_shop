# Dummy Shop 

## Django app + microservices 

The "Dummy Shop" App has been created for learning purposes. <br>
Objective was defined as development of a complex application from scratch using defined list of microservices run via docker containers
Detailed development log is [here](https://github.com/gorgeous-george/dummy_shop/blob/main/development_log.md)

## Common logic:
- There are two web-services named as "Shop" and "Storage".
- "Shop" emulates a book store and has primitive shopping cart
- "Storage" emulates a book storage that receives orders from the shop and fulfill them

## Architecture

- ![concept](/concept.png)
- '''data flow : synchronization, create order, update storage, return data''' TBD

## Quick Start

To get this project up and running locally on your computer:

- Set up Python 
- Set up Docker
- Add shop.env and storage.env files to the project's root with the following content (postgres db should be used)
  - DJANGO_SECRET_KEY=
  - DB_HOST=
  - DB_PORT=
  - DB_USER=
  - DB_PASSWORD=
  - DB_NAME=
- Run the following commands
```
docker-compose build
docker-compose up
```
- connect to "shop" and "storage" containers and run the following commands within each
```
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```
- Create some Books and Orders - please do it within http://127.0.0.1:8000/admin and http://127.0.0.1:8001/admin  

<br>Now the application is working
- To open the "SHOP" main page - open a browser to http://127.0.0.1:8000/
- To open the "STORAGE" API admin console - open a browser to http://127.0.0.1:8000/admin/
