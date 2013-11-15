Getting started using local environment.
```
$ git clone git@github.com:chriscabral/mythical-site.git
$ virtualenv venv --distribute
$ source venv/bin/activate
$ pip install -r requirements/project.txt
$ python manage.py createdb
$ python manage.py runserver 0.0.0.0:8000
```
Getting started using vagrant.
```
$ git clone git@github.com:chriscabral/mythical-site.git
$ vagrant up
$ vagrant ssh
$ virtualenv venv --distribute #might have some dependencies. (google is your friend)
$ source venv/bin/activate
$ pip install -r requirements/project.txt #might have some dependencies. (google is your friend)
$ python manage.py createdb #is a createdb and migrate with south all in 1.
$ python manage.py runserver 0.0.0.0:8000 #this is portforwared to 8001 in your local. 
```



Database migrations
-If a model has been changed than you have to create a schema migration with south
```
$ python manage.py migrate
$ python manage.py schemamigration project_manager --auto
$ python manage.py migrate 
$ git status
$ #find the migration files
$ git add [migration files]
$ git commit -m "some relavent commit"
$ git push origin master
```

Editing the pages on the screen
-If pages have been added and you would like those pages to go to production then:
```
$ python manage.py dumpdata pages --indent 4 > mezzanine/pages/fixtures/initial_data.json 
$ git add mezzanine/pages/fixtures/initial_data.json
$ git commit -m "some relavent commit message"
$ git push origin master
```

