git init
python2 -m virtualenv .venv
source ./.venv/bin/activate
pip install django==1.11
django-admin startproject hwproject
python manage.py startapp myapp
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
