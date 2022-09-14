# Dummy book shop 

## Django app + microservices 

The App has been created for learning purposes. <br>
Objective is to develop a complex application from scratch using defined list of microservices. 

## Architecture

- '''concept scheme picture''' https://app.terrastruct.com/diagrams/1464302938
- '''models scheme'''
- '''data flow : synchronization, create order, update storage, return data'''

## Quick Start

To get this project up and running locally on your computer:

- Set up the Python development environment. It is recommended to use a Python virtual environment.
- Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python3 to start Python):

```
'''to update this section!!!'''
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser # Create a superuser
python3 manage.py fill_db # to fill the database with lorem ipsum data
python3 manage.py runserver
```


Now the application is working
- To open the "SHOP" main page - open a browser to http://127.0.0.1:8000/
- To open the "STORAGE" API admin console - open a browser to http://127.0.0.1:8000/admin/

## Features:
- 1
- 2
- 
