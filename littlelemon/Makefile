.PHONY: all
all: up

# Build all services
.PHONY: build
build:
	docker compose build

# Start all services
.PHONY: up
up:
	docker compose up -d --build

# Stop all services
.PHONY: down
down:
	docker compose down --remove-orphans --volumes

# Stop all services and remove all containers
.PHONY: down-all
down-all:
	@if [ -n "$(shell docker ps -aq)" ]; then \
		for container in $(shell docker ps -aq); do \
			docker rm -f $$container; \
		done \
	fi

.PHONY: clean
clean:

	docker system prune -f --all --volumes

	docker network prune -f

	docker image prune -f

# Restart all services
.PHONY: re
re: down-all clean up
