Config File (Private)
=====================

https://docs.google.com/document/d/18Vgv92AUaqD5SP-NfiSkhYKIWQHZ1_YQEeTIcQb1a_k/edit?hl=en_US

Local Development Tips
======================

During local development, you now need to execute the following anytime you delete the database and start from scratch and remember to skip original creation of superuser:

    python manage.py syncdb
    python manage.py migrate
    python manage.py initializeproject
    python manage.py createsuperuser

Additionally, you will need to access the site in a specific way for the social auth to work: Add `dev.jaam.us.to` to your `HOSTS` file and point it at your development machine (usually `localhost` or `127.0.0.1`). Now you can access the development server through the new hostname, for example: http://dev.jaam.us.to:8000 after running the dev server.

Gondor (Just the) Tips
======================

**Gondor Configuration**: https://gondor.io/support/introduction/

**Make a Backup**: `gondor manage sqldump`

**Clear the Database**: `gondor manage primary database:clear`

**Deploy to Gondor**: `gondor deploy primary master`

**Initialize Project** (creates permissions/groups): `gondor run primary initializeproject`

** Create Admin User**: `gondor run primary createsuperuser`

Media/Static/Static_media Explained
===================================

* MEDIA
	* Uploaded user media
	* We will never use it
	* It was “wrong” of Ckeditor to want to be placed there.

* STATIC
	* Any static files go to this directory, THOUGH, you should never place anything there yourself.
	* The django.contrib.staticfiles app processes other applications static files and includes them were appropriate (this means that the django ckeditor was just written poorly, it should have been much, much, much, easier to use, in fact I’m tempted to patch it)

* STATIC_MEDIA
	* Is a directory I created for miscellaneous site media that we need to be able to serve for example, ckeditor

South Explained
===============

http://south.aeracode.org/docs/

After editing an Django model run:
    python manage.py schemamigration --auto APP_NAME

besides auto there is --add-field, --add-model, etc

If you need to change the data instead of the table structure, you can write a datamigration:
    python manage.py datamigration APP_NAME MIGRATION_NAME

A file will be created in the apps migration folder where you will add the code to modify the data.
When moving data into another column you might have to run a schemamigration to add the new column, a datamigration to move the data over, and another schemamigration to remove the old column.