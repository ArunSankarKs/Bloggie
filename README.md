# Bloggie
This is a simple Blog .

Make sure you have the following python packages :

    Django==2.2.5
    djongo==1.2.36
    Pillow==6.1.0
    pip==19.2.3

Then Makesure that you have your MongoDB up and Running 

open bloggie/settings.py  and Change the Database Credientials accordingly. (Username,Password,Dbname)

cd to this project directory and run "python manage.py makemigrations" (to record all the Database structure changes)

then run "python manage.py migrate" (to reflect all the changes done in your models to the MongoDb)

now run "python manage.py createsuperuser" (to create a SuperUser to your Page)

finally "python manage.py runserver" to run the server 

Good Luck :)
