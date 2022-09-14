***
### 1. Planning

***
### 2. Creation of project environment
Purpose is to create two separate folders each having separate virtual environment - for "shop" and "storage" microservices appopriately.
Pycharm is not able to create such structure. So that command line is used instead.

#### 2.1 Creation of Pycharm environment (folders, virtual environments, initial configurations)
-  moving to PycharmProjects directory
```
cd && cd PycharmProjects/
```
- creating a folder for the whole project
```
mkdir dummy_shop
```
- moving to the project's directory
```
cd dummy_shop
```
- creating a folder for the first microservice - "shop". It is supposed to be a django server
```
mkdir microservice_shop
```
- moving to "shop" directory with aim to create virtual environment within
```
cd microservice_shop
```
- creating virtual environment for "shop" microservice
```
python3 -m venv .venv_shop
```
- activation of the virtual environment for "shop" microservice
```
source .venv_shop/bin/activate
```
- updating pip for future use
```
pip install -U pip
```
- installing Django framework
```
pip install django
```
- starting a django project for "shop" microservice. Namely, it is creation of manage.py file and "core" directory containing main django settings
```
django-admin startproject core .
```
- creating initial "requirements.txt" file supposed to keep the list of all required relations/libraries
```
pip freeze > requirements.txt
```
- deactivation of the virtual environment
```
deactivate
```


- creating a folder for the second microservice - "storage". It is supposed to be a django REST API
```
mkdir microservice_storage
```
- moving to "storage" directory with aim to create virtual environment within
```
cd microservice_storage
```
- creating virtual environment for "storage" microservice
```
python3 -m venv .venv_storage
```
- activation of the virtual environment for "storage" microservice
```
source .venv_storage/bin/activate
```
- updating pip for future use
```
pip install -U pip
```
- installing Django framework
```
pip install django
```
- installing Django REST framework
```
pip install djangorestframework
```
- starting a django project for "storage" microservice. Namely, it is creation of manage.py file and "core" directory containing main django settings
```
django-admin startproject core .
```
- creating initial "requirements.txt" file supposed to keep the list of all required relations/libraries
```
pip freeze > requirements.txt
```
- deactivation of the virtual environment
```
deactivate
```

**That's it, now the project can be opened via Pycharm. <br> Each microservice will have its own virtual environment. <br>
There are a few ways to open the project in Pycharm:**
- open the root folder "dummy_shop" to manage it as consistent git repository
- open each microservice as a separate project
- open the first service and ***attach*** the second service to have them both executable from the same Pycharm window 

**To have django "shop" and django REST "storage" configurations both executable from the same Pycharm Window:**
- open first service (for example "microservice_shop" folder) as a new project
- open second service ("microservice_storage" folder) and select the option "Attach"
- open Settings/Project:"first_service name"/Python Interpreter and make sure that both services have interpretator selected/added
- open Settings/Project:"first_service name"/Project Dependencies and make sure that both services have no dependencies
- open Settings/Project:"first_service name"/Project Structure and make sure that both services have its virtual env folders marked as "Excluded"
- open Settings/Languages & Frameworks/Django and make sure that both services have enabled "Enable Django Support" and have "Django project root", "Settings" and "Manage script" selected/added appropriately
- open Run/Edit Configurations and create django server configuration for both services appropriately including name, project (selectable), interpreter and correct value of "DJANGO_SETTINGS_MODULE" environment variable

***Don't forget to secure the SECRET_KEYS***


***
#### 2.2 Creation and configuring git repository

- creating local git repository
```
git init
```
- creating README file for the repository
```
touch README.md
```
- creating .gitingore file to keep a particular project directories/files unpublished
```
touch .gitignore
```
- adding existed directories/files to git
``` 
git add .
```
- committing the README file to local git repository
```
git commit -m "initital commit"
```
- renaming branch from "master" to "main"
```
git branch -m main
```
- connection to remote github new repository that has been created preliminairy via github.com website
```
git remote add origin git@github.com:gorgeous-george/dummy_shop.git
```
- pushing the README file to remote repository 
```
git push -u origin main
```

!!!!! to add info about development branch, pull request, branch rules


***
### 3. Development



***
### 4. Testing



***
### 5. Implementing (deploy)



***
### 6. Post-implementation checks




