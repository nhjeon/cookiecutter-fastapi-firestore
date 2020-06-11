init:
	pip install pipenv
	pipenv run pipenv install --dev

check:
	isort -rc --check-only app
	black -S -l 79 --check app
	pylint app

format:
	isort -rc -y app
	black -S -l 79 app

run:
	GOOGLE_APPLICATION_CREDENTIALS=$(PWD)/serviceAccount.json PYTHONPATH=./app uvicorn main:app --reload

pytest:
	PYTHONPATH=./app python -m pytest

coverage:
	PYTHONPATH=./app python -m pytest ./test --cov app --cov-report term --cov-report xml

htmlcov:
	python -m pytest --cov app --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html

requirements:
	pipenv lock -r > requirements.txt
