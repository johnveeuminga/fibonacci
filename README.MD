# Fibonacci Nth Number Implementation in Django + Celery

A Django application that will calculate or display the Nth number in a Fibonacci sequence

## Running
1. On your terminal, run
`docker compose up -d`
2. If first time running, run migrations first:
`docker compose exec app python3 manage.py migrate`
* Note, you might need to wait a couple of seconds before running this command to finish Postgres initialization on first time start up
3. Base site is located at `http://localhost:8000`

## Tests
1. On your terminal, run
`docker compose exec app python3 manage.py test`
