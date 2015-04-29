# myhouse

Pan kazal zmienic:
- w zaleznosci od zapytania od uzytkownika daje dane XML
- LXML modul (niemcy napisali)
- moze warto powyzszy modul przetestowac ?
- kotchita wurst reklamuje sluchawki



At first, you must install django. You can make it with this commands:

a) sudo apt-get install python python-pip | sudo yum install python python-pip


##### now best solution is: #####

sudo pip install -r requirements.txt

##### end ######

or:

b) sudo pip install django==1.7

b1) sudo pip install django-admin-bootstrapped
b2) sudo pip install django-bootstrap3
b3) sudo pip install djangorestframework 
b4) sudo pip install markdown
b5) sudo pip install django-filter
b6) sudo pip install pygments 
b7) sudo pip install djangorestframework-xml

c) recommended is to use this command (in project directory)  python manage.py migrate && python manage.py syncdb


d) I have create superuser: admin with pass admin


=======================================================================

Moar stuff will be added later.


After changes in models.py that is required to run:

python manage.py makemigrations

python manage.py migrate

python manage.py syncdb

python manage.py runserver
