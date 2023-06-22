migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver

coverage:
	pytest --cov=dailyInbox --migrations -n 2 --dist loadfile

