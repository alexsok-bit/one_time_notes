args =
command =
repo = localhost
name = notes
tag = latest

env_dir = .venv
python = $(env_dir)/bin/python
pip = $(env_dir)/bin/pip

.PHONY: build run shell push stop clean setup all update

all:
	cp source/notes/settings/override.py.skeleton source/notes/settings/override.py
	cp docker-compose.yml.skeleton docker-compose.yml
	python3 -m venv $(env_dir)
	$(pip) install -r requirements.txt
	$(python) source/manage.py migrate
	$(python) source/manage.py collectstatic --no-input
	$(python) source/manage.py test

update:
	$(python) source/manage.py makemigrations $(args)
	$(python) source/manage.py migrate $(args)
	$(python) source/manage.py collectstatic --no-input
	$(python) source/manage.py $(args) test

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

clean: stop
	docker rmi $(repo)/$(name)
