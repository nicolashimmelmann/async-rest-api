# async-rest-api

This project shows one way of setting up an async REST API with a database
based on the following libraries:

- [`connexion`](https://github.com/spec-first/connexion)
- [`sqlalchemy`](https://github.com/sqlalchemy/sqlalchemy)
- [`asyncpg`](https://github.com/MagicStack/asyncpg)

The database session is instantiated per request in a custom ASGI middleware
and stored in a context variable scoped to the current async task which
processes the request.

## How to run

The whole setup can be run with Docker:

```bash
docker compose build
docker compose up
```

The API will listen on `http://127.0.0.1:8080/api/v1`.

## Sending simple requests

Write a new user:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"username": "Max"}' \
  http://127.0.0.1:8080/api/v1/user
```

Read all users:

```bash
curl -X GET http://127.0.0.1:8080/api/v1/user
```

## Viewing the database

For simplicity, I have added a container with pgadmin to the docker compose
file. Using that tool, you can easily view the database contents by opening a
web browser at `http://127.0.0.1:8081`
