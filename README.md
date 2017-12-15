USED COMMANDS:
git init
python2 -m virtualenv .venv
source ./.venv/bin/activate
pip install django==1.11
django-admin startproject hwproject
python manage.py startapp myapp
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
git add *
git commit -m "commit"
git remote add origin https://github.com/IstanbulSehirUniversity2017Fall/assignment1-django-models-SharpThunder.git
git push -u origin master
