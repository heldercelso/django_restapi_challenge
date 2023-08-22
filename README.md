## Introduction

This project implements a REST API developed in Django with PostgreSQL database and aims to
cover all cases of the `BrasilPrev` challenge (API to store Clients, Contracts and Plans).
The details can be found on the pdf file `Desafio Técnico Brasilprev -- Backend.pdf`.


## Technologies

Back-end (API):
 - Django Rest Framework `3.13` (Python `3.7`).

Other technologies used:
 - Docker;
 - PostgreSQL.

### Structure

```shell
.
├── django-rest-api                                                       # Django project (python)
│   ├── client_api
│   │   ├── migrations                                                    # Django ORM migrations
│   │   ├── tests
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                                                     # Modeling database
│   │   ├── serializers.py                                                # Validating fields
│   │   ├── urls.py                                                       # Defining endpoints
│   │   ├── utils.py
│   │   └── views.py                                                      # Endpoints logic
│   ├── contract_api
│   │   ├── migrations                                                    # Django ORM migrations
│   │   ├── tests
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                                                     # Modeling database
│   │   ├── serializers.py                                                # Validating fields
│   │   ├── urls.py                                                       # Defining endpoints
│   │   ├── utils.py
│   │   └── views.py                                                      # Endpoints logic
│   ├── plans_api
│   │   ├── migrations                                                    # Django ORM migrations
│   │   ├── tests
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py                                                     # Modeling database
│   │   ├── serializers.py                                                # Validating fields
│   │   ├── urls.py                                                       # Defining endpoints
│   │   ├── utils.py
│   │   └── views.py                                                      # Endpoints logic
│   ├── project_core                                                      # Django core settings
│   │   ├── asgi.py
│   │   ├── settings.py                                                   # General project settings
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── conftest.py
│   ├── docker-entrypoint.sh                                              # Entrypoint to start database migrations when starting the project
│   ├── Dockerfile                                                        # Dockerfile to build
│   ├── manage.py
│   ├── pytest.ini
│   └── requirements.txt                                                  # Libraries
│
├── database_diagram.png                                                  # Database diagram
├── postgres_data_django                                                  # Database generated after initialized
├── docker-compose.yaml                                                   # Compose file for django
└── README.md
```


## Running the project:

To run the project is necessary to have `docker` and `docker-compose` installed in your environment.

```shell
# To build the Django application:
$ docker-compose build

# Initializing the project:
$ docker-compose up
```

From that point on, all containers will be available.
To access the application, just open the address `http://localhost:8080/api/v1/<endpoint>` in your browser. You can see the documentation below for more details.


## Development

The structure contained in the `docker-compose.yaml` file provides distinct containers for:
* API (Django);
* Database (PostgreSql).

### API Documentation:

This project consists of three APIs: clients, contracts and plans.

`Swagger` is implemented through drf-yasg library and can be accessed in:
* `http://localhost:8080/api/v1/swagger/schema/`

For direct access (`DRF - Django Rest Framework`) use the following endpoints:
* `http://localhost:8080/api/v1/clients`
* `http://localhost:8080/api/v1/client/<pk>/`
* `http://localhost:8080/api/v1/contracts`
* `http://localhost:8080/api/v1/contract/<pk>/`
* `http://localhost:8080/api/v1/deposits`
* `http://localhost:8080/api/v1/deposit/<pk>/`
* `http://localhost:8080/api/v1/withdraws`
* `http://localhost:8080/api/v1/withdraw/<pk>/`
* `http://localhost:8080/api/v1/plans`
* `http://localhost:8080/api/v1/plan/<pk>`

### Database

The model diagram can be seen in the root directory of this project as `database_diagram.png`.

Command to generate database diagram (it needs django-extensions and pygraphviz libs):
```shell
$ docker exec -ti web python manage.py graph_models client_api contract_api plans_api -g -o database_diagram.png
```

## Tests

To run the tests, simply enter the following commands in your terminal:

```shell
# Initialize the project:
$ docker-compose up

# Run the tests:
$ docker exec -ti web pytest -vx
```