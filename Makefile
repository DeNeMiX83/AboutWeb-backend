include deploy/.env

# run:
# 	make run-backend

# run-backend:
# 	poetry run gunicorn app.interfaces.api.main:app --reload --bind $(HOST):$(DOCKER_BACKEND_PORT)
	
# compose-build:
# 	docker-compose -f ./deploy/docker-compose.yml --env-file ./deploy/.env build

# compose-up:
# 	docker-compose -f ./deploy/docker-compose.yml -p $(PROJECT_NAME) --env-file deploy/.env up

# compose-down:
# 	docker-compose -f ./deploy/docker-compose.yml -p $(PROJECT_NAME) --env-file deploy/.env down

# compose-restart:
# 	docker-compose -f ./deploy/docker-compose.yml -p $(PROJECT_NAME) --env-file deploy/.env restart

# compose-logs:
# 	docker-compose -f ./deploy/docker-compose.yml -p $(PROJECT_NAME) --env-file deploy/.env logs -f

migrate-create:
	echo ${POSTGRES_DB} && poetry run alembic -c deploy/alembic.ini revision --autogenerate

migrate-up:
	poetry run alembic -c deploy/alembic.ini upgrade head