build:
	docker-compose build

run:
	docker-compose up

migrations:
	docker-compose run --rm task_manager python3 manage.py makemigrations

migrate:
	docker-compose run --rm task_manager python3 manage.py migrate

shell:
	docker-compose run --rm task_manager python3 manage.py shell

bash:
	docker-compose run --rm task_manager /bin/bash

