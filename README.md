# mainak-django-tenant-schemas

## Description
- Django polls app implemented as a REST API with a multi tenant architecture


## Setting up
#### Prerequisites
- Postgres instance installed on your machine
- Git

## Set up locally
- Clone the repository and `cd` into the folder
- Create a virtual environment
- Install all dependecies in the `requirements.txt`

## Migrations
- Create a Posgtres DB and add the DB information to your `.env` file which should be based of the `.env_example` attached to this repository
- Load the `.env` variables by running `source .env`
- Run migrations `python manage.py makemigrations`
- Migrate `python manage.py migrate_schemas` 

## Running the Server
- Run the server `python manage.py runserver`
