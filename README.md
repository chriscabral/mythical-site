
Database migrations
-If a model has been changed than you have to create a schema migration with south
    $ python manage.py migrate
    $ python manage.py schemamigration project_manager --auto
    $ python manage.py migrate 
    $ git status
    find the migration files
    $ git add [migration files]
    $ git commit -m "some relavent commit"
    $ git push origin master


This process does not work. todo look for a better solution like django-smuggler
Editing the pages on the screen
-If pages have been added and you would like those pages to go to production then:
    $ python manage.py dumpdata --natural --exclude contenttypes --exclude auth --exclude sessions --exclude sites --exclude pages --exclude twitter --exclude south > initial_data.json
    $ git add initial_data.json
    $ git commit -m "some relavent commit message"
    $ git push origin master


