***
### 1. Planning
- analysis of the project purpose and architecture
- drafting models, views, page templates

***
### 2. Creation of project environment
- Install python
- Install Pycharm software <br>
Now, the purpose is to create two separate folders each having separate virtual environment - for "shop" and "storage" microservices appropriately. <br>
Pycharm is not able to create such structure. So that command line is used instead.

#### 2.1 Creation of Pycharm environment via command line (folders, virtual environments, initial configurations)
- open the terminal on Ubuntu
- moving to PycharmProjects directory
- creating a folder for the whole project
```
$ cd && cd PycharmProjects/
$ mkdir dummy_shop
```
- moving to the project's root directory
- creating a folder for the first microservice - "shop". It is supposed to be a django server
- moving to "shop" directory with aim to create virtual environment within
- creating virtual environment for "shop" microservice
- activation of the virtual environment for "shop" microservice
```
$ cd dummy_shop
$ mkdir microservice_shop && cd microservice_shop
$ python3 -m venv .venv_shop
$ source .venv_shop/bin/activate
```
- updating pip for future use
- installing Django framework
- installing required libraries such as Pillow (work with pictures)
- starting a django project for "shop" microservice. Namely, it is creation of manage.py file and "core" directory containing main django settings
- creating initial "requirements.txt" file supposed to keep the list of all required relations/libraries
- deactivation of the virtual environment
```
$ pip install -U pip
$ pip install django
$ pip install Pillow
$ django-admin startproject core .
$ pip freeze > requirements.txt
$ deactivate
```
- moving to project's root directory
- creating a folder for the second microservice - "storage". It is supposed to be a django REST API
- moving to "storage" directory with aim to create virtual environment within
- creating virtual environment for "storage" microservice
- activation of the virtual environment for "storage" microservice
```
$ cd && cd PycharmProjects/dummy_shop
$ mkdir microservice_storage
$ cd microservice_storage
$ python3 -m venv .venv_storage
$ source .venv_storage/bin/activate
```
- updating pip for future use
- installing Django framework
- installing Django REST framework
- starting a django project for "storage" microservice. Namely, it is creation of manage.py file and "core" directory containing main django settings
- creating initial "requirements.txt" file supposed to keep the list of all required relations/libraries
- deactivation of the virtual environment
```
$ pip install -U pip
$ pip install django
$ pip install djangorestframework
$ pip install markdown
$ pip install django-filter
$ django-admin startproject core .
$ pip freeze > requirements.txt
$ deactivate
```

That's it, now the project can be opened via Pycharm. Each microservice will have its own virtual environment. <br>
**There are a few ways to open the project in Pycharm:**
- open the root folder "dummy_shop" to manage it as consistent Git repository
- open each microservice as a separate project
- open the first service and ***attach*** the second service to have them both executable from the same Pycharm window 

**To have django "shop" and django REST "storage" configurations both executable from the same Pycharm Window:**
- open first service (for example "microservice_shop" folder) as a new project
- open second service ("microservice_storage" folder) and select the option "Attach"
- open Settings/Project:"first_service name"/Python Interpreter and make sure that both services have interpreter selected/added
- open Settings/Project:"first_service name"/Project Dependencies and make sure that both services have no dependencies
- open Settings/Project:"first_service name"/Project Structure and make sure that both services have its virtual env folders marked as "Excluded"
- open Settings/Languages & Frameworks/Django and make sure that both services have enabled "Enable Django Support" and have "Django project root", "Settings" and "Manage script" selected/added appropriately
- open Run/Edit Configurations and create django server configuration for both services appropriately including name, project (selectable), interpreter and correct value of "DJANGO_SETTINGS_MODULE" environment variable
- add alternative dummy databases to run the services outside the docker container (SQLite is an option)

***Don't forget to secure the SECRET_KEYS***

***
#### 2.2 Installing Docker

- open the terminal on Ubuntu
- remove any Docker files that are running in the system
- check if the system is up-to-date
- install Docker
- install all the dependency packages
- before testing Docker, check the version installed
- pull an image from the Docker hub
- check if the docker image has been pulled and is present in your system
- display all the containers pulled
- check for containers in a running state

```
$ sudo apt-get remove docker docker-engine docker.io
$ sudo apt-get update
$ sudo apt install docker.io
$ sudo snap install docker
$ docker --version
$ sudo docker run hello-world
$ sudo docker images
$ sudo docker ps -a
$ sudo docker ps
```

That's it, Docker is successfully installed on Ubuntu!

***
#### 2.3 Creation and configuring git repository

- creating new repository at GitHub to have it as remote repository
- creating and configuring SSH keys
- configuring branch protection rules for "main" branch at least
> https://github.com/gorgeous-george/dummy_shop
- creating local git repository
- creating README file for the repository
- creating .gitingore file to keep a particular project directories/files unpublished
- adding existed directories/files to git
- committing the README file to local git repository
- renaming branch from "master" to "main"
- connection to remote GitHub new repository that has been created preliminary via github.com website
- pushing the README file to remote repository 
- creating local branch "develop" && switching to it && adding files to git tracker
```
cd && cd PycharmProjects/dummy_shop
git init
touch README.md
touch .gitignore
git add .
git commit -m "initial commit"
git branch -m main
git remote add origin git@github.com:gorgeous-george/dummy_shop.git
git push -u origin main
git branch develop && git checkout develop && git add .
```

That's it, local Git repository has been created and connected to remote GitHub repository. <br>

**Code committing and pushing workflow is supposed to be the following:**
- Code development is performed within separate local branch "develop". Local commits are created and then pushed to GitHub branch "develop"
```
git branch develop && git checkout develop
git add .
git status
git commit -m 'commit message'
git push --set-upstream origin develop
```
- At GitHub a pull request is created to merge branch "develop" to branch "main"
- GitHub branch "develop" is deleted
- Local branch "main" is synchronized with GitHub branch "main"
- Local branch "develop" is deleted
```
git checkout main && git pull
git branch --delete develop
```
- Back to the first step

***
#### 2.4 Containerization - configuring docker and docker-compose

- creating folder "docker" to have all settings there
- creating folders "shop" and "storage" for each service appropriately
- creating Dockerfile for each service (can be also "service_name".Dockerfile)
```
cd && cd PycharmProjects/dummy_shop
mkdir docker && cd docker
mkdir shop && cd shop
touch Dockerfile
cd .. && mkdir storage && cd storage
touch Dockerfile
```
- adding configurations to Dockerfiles appropriately for "shop" and "storage"
> shop/Dockerfile <br>
> storage/Dockerfile

- creating .env files to keep sensitive data required by docker-compose (DJANGO_SECRET_KEY and DB credentials)
```
cd && cd PycharmProjects/dummy_shop
touch shop.env
touch storage.env
```
- adding the shop.env and storage.env files to .gitignore <br><br>

- creating docker-compose.yml file
```
cd && cd PycharmProjects/dummy_shop
touch docker-compose.yml
```
- configuring docker-compose.yml 
> docker-compose.yml <br><br>
> services:
> - shop
> - storage
> - db_shop
> - db_storage
> - nginx
> - mailhog
> - pgadmin
> - flower
> - redis
> - rabbitmq
<br><br>
>
> networks:
> 
> volumes:

- building and running up the docker-compose
```
sudo docker-compose build
sudo docker-compose up
...
CTRL+C
sudo docker-compose down
```

***
#### 2.5 Configuring database layer
- installing DB PostgreSQL for "shop" service (***the same steps performed for "storage" service***)
  - installing psycopg library
  ```
  cd && cd PycharmProjects/dummy_shop/microservice_shop
  source .venv_shop/bin/activate
  pip install psycopg2-binary
  pip freeze > requirements.txt
  ```
  - updating "microservice_shop/core.settings" - DATABASES
  - adding appropriate DATABASE credentials to "shop.env" file
  - adding appropriate sections to "django-compose.yml"
  - creating "docker-entrypoint.sh" and "wait-for-command.sh" to check that db is up before running services dependent on db
  - updating Dockerfile
  - building and running up the docker-compose
  <br>

  - connecting to docker container's bash terminal and running migrations
  ```
  sudo docker-compose exec shop bash
  ./manage.py makemigrations
  ./manage.py migrate
  ./manage.py createsuperuser
  exit
  ``` 
  
  <br>
  
  - to shut the docker-compose down the following command is used
  ```
  CTRL+C
  sudo docker-compose down
  ```

***
#### 2.6 Configuring django extensions and tools:
- django-debug-toolbar for both "shop" and "storage" services (https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
- django-extensions for both "shop" and "storage" services (https://django-extensions.readthedocs.io/en/latest/installation_instructions.html)
- graph_models for both "shop" and "storage" services (https://django-extensions.readthedocs.io/en/latest/graph_models.html)
- django-celery-beat scheduler for "shop" service (https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#beat-custom-schedulers)
- django-redis-cache for "shop" service (https://django-redis-cache.readthedocs.io/en/latest/intro_quick_start.html)

***
#### 2.7 Configuring the microservices as docker containers
- celery for "shop" service (https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html)
  - installation, updating requirements, 
  - updating core.settings, 
  - __init.py__, 
  - creating celery.py, 
  - tasks.py, 
  - add appropriate sections to "django-compose.yml"
- rabbitmq for "shop" service (as broker for celery), add appropriate sections to "django-compose.yml"
- redis cache, add appropriate sections to "django-compose.yml"
- pgadmin, add appropriate sections to "django-compose.yml" 
- nginx, add appropriate sections to "django-compose.yml"
- flower, add appropriate sections to "django-compose.yml" 
- mailhog, add appropriate sections to "django-compose.yml"

***
### 3. Development

Creating new apps, models, views, etc. - don't forget to switch ".venv_shop" and ".venv_storage" virtual environments appropriately 

#### 3.1 "Shop" service

##### Creating apps

- creating applications for "shop" : "auth_shop", "book", "order"
```
source microservice_shop/.venv_shop/bin/activate
cd microservice_shop
./manage.py startapp auth_shop
./manage.py startapp book
./manage.py startapp order
deactivate
```
- adding new applications to INSTALLED_APPS in "shop" settings

##### Creating models

- creating/updating models for "shop"
  - proxy User 
  - Book 
  - Order
  - OrderItem
  - ![graph](https://github.com/gorgeous-george/dummy_shop/blob/main/microservice_shop/shop_models_graph.png)
- registering models at admin.py
- rebuilding docker-compose
- connecting to "shop" container to apply migrations


##### Creating views

- **"auth_shop"** application
  - index
  - user profile
  - user register
  - user profile update
  - *other auth views (password reset, login, logout) are standard django views*
- **"book"** application
  - book list
  - book detail (implementing @cache_page decorator)
- **"order"** application 
  - cart create
  - order detail
  - order confirm

##### Creating templates

- update settings.py to have the only one base_generic.html for all applications
  ```
  'DIRS': [os.path.join(BASE_DIR, 'templates')], 
  ```
- creation of base_generic.html template, saving it to dummy_shop/microservice_shop/templates
- creation of index.html for homepage
  
- **"auth_shop"** application
    - register
    - login
    - logged_out
    - profile
    - update_profile
    - password_reset_complete
    - password_reset_confirm
    - password_reset_done
    - password_reset_email
    - password_reset_form
  
- **"book"** application
  - book_list
  - book_detail
  
- **"order"** application
  - order_detail
  - order_confirm
  - orderitem_list
  - orderitem_form

##### Creating forms

- register form (auth_shop/forms.py)
- order create form (order/views)
- order confirm form (order/forms.py)

##### Configuring urls

- core: '', admin, accounts, includes (auth, book, order), debugtoolbar
- book: shop_books, shop_book_detail
- order: cart_create, shop_cart, order_confirm 

#### 3.2 "Storage" service

##### Creating apps

- creating applications for "storage" : "book", "order"
```
source microservice_storage/.venv_storage/bin/activate
cd microservice_storage
./manage.py startapp book
./manage.py startapp order
```
- adding new applications to INSTALLED_APPS in "storage" settings

##### Creating models

- creating/updating models for "storage"
  - Book
  - BookItem
  - Order
  - OrderItem
  - ![graph](https://github.com/gorgeous-george/dummy_shop/blob/main/microservice_storage/storage_models_graph.png)
- registering models at admin.py
- rebuilding docker-compose
- connecting to "storage" container to apply migrations

##### Creating views

- **"book"** application
  - BookViewSet
  - BookItemViewSet
  
- **"order"** application
  - OrderViewSet
  - OrderItemViewSet

##### Creating serializers

- **"book"** application
  - BookSerializer
  - BookItemSerializer
  
- **"order"** application
  - OrderSerializer
  - OrderItemSerializer

##### Configuring urls

- core
- book
- order

***
### 4. Developing business logic and appropriate Celery tasks

- Shop: POST "order placement" request from "shop" to "storage" - Order, OrderItems:{id, client, delivery_address}, {book, quantity} 
- Shop: GET synchronization request from "shop" to "storage" on book.left_in_stock 
- Shop: GET request from "shop" to "storage" - Order:{id, status} and sending email to client for succeeded orders
- Storage book.views: synchronization of available book items with book.left_in_stock
- Storage book.views: book items' statuses update after order fulfillment

***
### 5. Testing

TBD

***
### 6. Implementing (deploy)

TBD 

***
### 7. Post-implementation checks

TBD