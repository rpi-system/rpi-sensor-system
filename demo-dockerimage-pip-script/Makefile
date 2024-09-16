.PHONY: info locenv start run build

IMAGE_NAME = rpi-temperature
DOCKERFILE = Dockerfile
CONTAINER_NAME = rpi-temperature
CPU_LIMIT = "0.5"
MEMORY_LIMIT = "256m"

info:
	@echo "IMAGE_NAME: $(IMAGE_NAME)"
	@echo "DOCKERFILE: $(DOCKERFILE)"
	@echo "CONTAINER_NAME: $(CONTAINER_NAME)"
	@echo "CPU_LIMIT: $(CPU_LIMIT)"
	@echo "MEMORY_LIMIT: $(MEMORY_LIMIT)"

locenv:
	@echo "Creating local environment"
	python3 -m venv .venv
	@echo "Installing requirements"
	.venv/bin/pip install -r requirements.txt
	@echo "Activating local environment"
	@echo "source .venv/bin/activate"

start:
	@echo "Starting the application"
	.venv/bin/python3 app.py

build:
	docker build --no-cache -t $(IMAGE_NAME) -f $(DOCKERFILE) .
	
run: 
	docker run --rm --name $(CONTAINER_NAME) --cpus=$(CPU_LIMIT) --memory=$(MEMORY_LIMIT) -d $(IMAGE_NAME)
	sleep 5
	docker logs -f $(CONTAINER_NAME)
