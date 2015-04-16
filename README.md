This app is writen in python 2.7 and django 1.7

1. Fake service has dumped data from database to XML and give it on site (myhouse)
2. Apartment finder can read and add to database data from fake service (myhouse)
3. Retrieve data from Otodom API
4. This app can add data to own site
5. Apartment finder can find duplicate ads.
6. App can search and sort ads.
7. Hurrey!





At first, you must install django. You can make it with this commands:

a) sudo apt-get install python python-pip | sudo yum install python python-pip

b) sudo pip install django==1.7

b1) sudo pip install django-admin-bootstrapped 

b2) sudo pip install django-bootstrap3

c) recommended is to use this command (in project directory) python manage.py migrate && python manage.py syncdb

d) I have create superuser: admin with pass admin



Moar stuff will be added later.

After changes in models.py that is required to run:

python manage.py makemigrations

python manage.py migrate

python manage.py syncdb

python manage.py runserver
