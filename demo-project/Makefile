.PHONY: info locenv start run build logs

IMAGE_NAME = rpi-temperature
DOCKERFILE = Dockerfile
CONTAINER_NAME = rpi-temperature
CPU_LIMIT = "0.5"
MEMORY_LIMIT = "256m"

locenv:
	@echo "Creating local environment in env/.venv folder"
	python3 -m venv env/.venv
	@echo "Installing requirements"
	env/.venv/bin/pip install -r requirements.txt
	@echo "Copying app.py into the environment"
	cp app.py env/app.py
	@echo "Activating local environment"
	@echo "source env/.venv/bin/activate"

start:
	@echo "Starting the application"
	env/.venv/bin/python3 env/app.py

run: 
	docker run --rm --name $(CONTAINER_NAME) --cpus=$(CPU_LIMIT) --memory=$(MEMORY_LIMIT) -d $(IMAGE_NAME)

logs:
	docker logs -f $(CONTAINER_NAME)

build:
	DOCKER_BUILDKIT=1 docker build --no-cache -t $(IMAGE_NAME) -f $(DOCKERFILE) .

cronjob: 
	crontab -e */2 * * * * /usr/bin/python ./app.py