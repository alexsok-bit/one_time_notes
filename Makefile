args =
command =
repo = localhost
name = notes
tag = latest

.PHONY: build run shell push stop clean

build:
	docker build $(args) -t $(repo)/$(name):$(tag) .

run:
	docker run --name $(name) --rm $(args) -p 127.0.0.1:8000:8000 $(repo)/$(name):$(tag)

shell:
	docker run --entrypoint /bin/bash --name $(name) --rm -ti $(args) $(repo)/$(name):$(tag)

push:
	docker login https://$(repo)
	docker push $(repo)/$(name):$(tag)

stop:
	docker stop $$(docker ps -ql)

clean:
	docker rmi $(repo)/$(name)
