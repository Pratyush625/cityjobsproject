To run locally, do the usual:

#. Create a Python 3.6 virtualenv Django 1.11 version installed

#. Create project projectname 
   
    django-admin startproject jobsproject

#. Go to the project dir 
   
    cd jobsproject

#. Create application inside main project directory 

    py manage.py startapp testapp

#. Configure the templatefile and staticfile inside settings.py 

#.Create template folder and static folder, inside static folder create css folder and image folder, insert the required images, Here sqlite used as default database

#. Create 4 different model class for 4 different cities with attributes

#. To convert model class to sql code use makemigrations 

    py manage.py makemigrations

#. To create table inside database 

    py manage.py migrate

#. Create superuser to connect with database 

    py manage.py createsuperuser

#. Register the model class inside admin.py file
   
    admin.site.register(model,modeladmin)



#. Define view function inside views.py 

#. To show end user of existing database data
    
    modelname.objects.all()
    
#. One populate.py script has been created for generating multiple records at a time using Faker Module

#. Define view function inside urls.py

#. To run server 

    py manage.py runserver
