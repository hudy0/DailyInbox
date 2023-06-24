migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate
	#python3 manage.py runserver

coverage:
	pytest --cov=dailyInbox --migrations -n 2 --dist loadfile

# Generate an image of the models in the system.
graph:
	python3 manage.py graph_models
