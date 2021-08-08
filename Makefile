serve:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations $(app name)

collectstatic:
	python3 manage.py collectstatic=1

app:
	#django-admin startapp <name>
	python manage.py startapp $(app name)

check:
	python manage.py check

test:
	python run ./manage.py test

superuser:
	python ./manage.py createsuperuser
