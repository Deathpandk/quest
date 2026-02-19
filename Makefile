install:
	pip install -r requirements.txt

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