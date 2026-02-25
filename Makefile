install:
	pip install -r requirements.txt
	pre-commit install

format:
	isort .
	black .
	autoflake .

check:
	black . --check
	isort .  --check
	autoflake . --check-diff
	python manage.py makemigrations --dry-run --check
	python manage.py test --noinput

run:
	python manage.py runserver

test:
	python manage.py test
