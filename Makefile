APP_NAME="neuromorphic-checkpoint-two"
IMAGE_NAME="eduardomatoss/neuromorphic-checkpoint-two"
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    DOCKER_USER=$(shell id -u $(USER)):$(shell id -g $(USER))
endif
ifeq ($(UNAME_S),Darwin)
    DOCKER_USER=
endif

################################
# COMMANDS TO RUN LOCALLY
################################

local/install: generate-default-env-file
	poetry install

local/lint:
	poetry run flake8 .
	poetry run black --check .

local/run:
	poetry run streamlit run run.py


############################################
# COMMANDS TO RUN USING DOCKER (RECOMMENDED)
############################################

docker/build: generate-default-env-file
	docker-compose build ${APP_NAME}

docker/up:
	docker-compose up -d

docker/down:
	docker-compose down --remove-orphans

docker/lint:
	docker-compose run ${APP_NAME} poetry run flake8 .
	docker-compose run ${APP_NAME} poetry run black --check .

docker/run:
	docker-compose run ${APP_NAME} poetry run streamlit run run.py

docker/migrations/generate:
	CURRENT_UID=${DOCKER_USER} docker-compose run ${APP_NAME} alembic revision --autogenerate

docker/migrations/upgrade:
	CURRENT_UID=${DOCKER_USER} docker-compose run ${APP_NAME} alembic upgrade head

##################
# HELPFUL COMMANDS
##################

image/build:
	docker build . --target production -t ${IMAGE_NAME}:${VERSION}

image/push:
	docker push ${IMAGE_NAME}:${VERSION}

generate-default-env-file:
	@if [ ! -f .env ]; then cp env.template .env; fi;
