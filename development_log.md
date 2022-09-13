***
### 1. Creation of project environment via commnad line

#### 1.1 Creation of Pycharm environment (folders, virtual environments, initial configrutaions)
- cd	
- cd PycharmProjects/			# moving to PycharmProjects directory
- mkdir dummy_shop			# creating a folder for the whole project
- cd dummy_shop			# moving to the project's directory

- mkdir microservice_shop		# creating a folder for the first microservice - "shop". It is supposed to be a django server
- cd microservice_shop			# moving to "shop" directory with aim to create virtual environment within
- python3 -m venv .venv_shop		# creating virtual environment for "shop" microservice
- source .venv_shop/bin/activate	# activation of the virtual environment for "shop" microservice
- pip install -U pip			# updating pip for future use
- pip install django			# installing Django framework
- django-admin startproject core .	# starting a django project for "shop" microservice. Namely, it is creation of manage.py file and "core" directory containing main django settings
- pip freeze > requirements.txt	# creating initial "requirements.txt" file supposed to keep the list of all required relations/libraries
- deactivate				# deactivation of the virtual environment

- mkdir microservice_storage		# creating a folder for the second microservice - "storage". It is supposed to be a django REST API
- cd microservice_storage		# moving to "storage" directory with aim to create virtual environment within
- python3 -m venv .venv_storage	# creating virtual environment for "storage" microservice
- source .venv_storage/bin/activate	# activation of the virtual environment for "storage" microservice
- pip install -U pip			# updating pip for future use
- pip install django			# installing Django framework
- pip install djangorestframework	# installing Django REST framework
- django-admin startproject core .	# starting a django project for "storage" microservice. Namely, it is creation of manage.py file and "core" directory containing main django settings
- pip freeze > requirements.txt	# creating initial "requirements.txt" file supposed to keep the list of all required relations/libraries
- deactivate				# deactivation of the virtual environment


***
#### 1.2 Creation and configuring git repository

- git init				# creating local git repository
- touch README.md			# creating README file for the repository
- touch .gitignore			# creating .gitingore file to keep a particular project directories/files unpublished
- git add .				# adding existed directories/files to git
- git commit -m "initital commit"	# committing the README file to local git repository
- git branch -m main			# renaming branch from "master" to "main"
- git remote add origin git@github.com:gorgeous-george/dummy_shop.git	# connection to remote github new repository that has been created preliminairy via github.com website
- git push -u origin main		# pushing the README file to remote repository




