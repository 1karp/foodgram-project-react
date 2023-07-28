![foodgram-project-react Workflow Status](https://github.com/1karp/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=master&event=push)

# Foodgram - Grocery Assistant

After launching the project, it will be available at your address. See below for instructions on how to run and view it in action.

## Description of the Foodgram Project

"Foodgram" is an application where users can publish recipes of culinary delights, subscribe to publications from other authors, and add recipes to their favorites. The "Shopping List" service allows users to create a list of products needed to prepare selected dishes according to the recipe(s).

## Project Setup and Launch

### Clone the repository to your local machine:

```
git clone https://github.com/1karp/foodgram-project-react
```


* Create a .env file and enter the following information:
    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<name of the PostgreSQL database>
    DB_USER=<database user>
    DB_PASSWORD=<password>
    DB_HOST=<db>
    DB_PORT=<5432>
    SECRET_KEY=<django project secret key>
    ```
  
* On the server, build the docker-compose:
```
sudo docker-compose up -d --build
```

* After successful build on the server, execute the following commands (only after the first deployment):
    - Collect static files:
    ```
    sudo docker-compose exec backend python manage.py collectstatic --noinput
    ```
    - Apply migrations:
    ```
    sudo docker-compose exec backend python manage.py migrate --noinput
    ```
    - Create a Django superuser:
    ```
    sudo docker-compose exec backend python manage.py createsuperuser
    ```
    - The project will be available at your IP address.
