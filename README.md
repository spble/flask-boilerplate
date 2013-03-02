flask-boilerplate
=================

A nice starting point for most of my web projects, using Flask.

Firstly, I suggest you create a virtualenv:
    
    $ virtualenv <some_name>

Install the pip requirements,

    $ ./<env_name>/bin/pip install -r requirements.txt

If you are going to be running this Flask server in debug mode (non-production), I suggest you change config.py to DEBUG=True

To start the server,

    $ ./<env_name>/bin/python manage.py runserver
    * Running on http://127.0.0.1:5000/

Visit http://127.0.0.1:5000/ in your browser.

There is also an example module that exists in case the use case for the flask app is to have multiple modules (e.g. an admin panel, separate from the main app logic). You can currently access this via the /module/ route, that is, http://127.0.0.1:5000/module/







