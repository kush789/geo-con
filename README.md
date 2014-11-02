GEO-CON
==========

Geo-Con is a django based social netwroking site in which you can post your thoughts, view other people's post, like posts, comment and much more!
It was developed as the project for the hackathon at PECFEST 2014.
FEATURES
========

In no particular order:

- Searching for locations across the world and getting their details which is usually overlooked by the popular tourism sites, as it is derived by the posts of the users of the site.
- Post which includes Location, Summary, Images Uploads, the local languages,food, local artists and must visit spots. 
- View all posts of a specific person
- Like posts
- Comment on posts
- Like Comment
- Delete your posts and comment
- Follow people. Their posts are highlighted on the right side of your Newsfeed

TECH
====

This application uses:

-Python Django
-Bootstrap
-Bootstrap3
-Social Auth (Google Oauth2)
-Google Maps API

INSTALLATION
============

Assuming you already have git-core and django installed

1. git clone https://github.com/kush789/geo-con.git
2. cd geo-con
3. register this app on google console for google oauth2 key
4. open settings.py and type in the oauth client id and secret
3. sudo apt-get install python-pip
3. sudo pip install django-bootstrap-form
4. sudo pip install django-bootstrap3
5. sudo pip install django-social-auth
6. python manage.py makemigrations
7. python manage.py syncdb
8. python manage.py runserver
9. Open browser and type 127.0.0.1:8000 (Or localhost:8000/ )

AUTHOR
======

Lohitaksh Parmar, Kushagra Singh, Nalin Gupta

IIIT Delhi | Btech 1st year 






