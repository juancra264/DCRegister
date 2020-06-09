APP_NAME ?= "dcregister"
VERSION ?= "v0.0.1"

help: ## Print this help.help: 
	    @grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Build a Dockerimage
	docker build -t $(APP_NAME):$(VERSION) .

