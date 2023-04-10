.PHONY: setup \
		init_db \
        up_db \
        down_db \
        run


install:
	python3 -m venv .venv

setup: install
	. .venv/bin/activate; pip install --upgrade pip
	. .venv/bin/activate; pip install -r src/requirements.txt

init_db: install
	. .venv/bin/activate; python src/manage.py makemigrations
	. .venv/bin/activate; python src/manage.py migrate

up_db:
	docker-compose -f docker/docker-compose.yml up db -d --build

down_db:
	docker-compose -f docker/docker-compose.yml down

drop_db:
	docker-compose -f docker/docker-compose.yml down -v

run: .venv/bin/activate
	python src/manage.py runserver
