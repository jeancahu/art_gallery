# Art Gallery

Django backend.<br>
Nginx web server.<br>
Spatial by [TEMPLATED](https://templated.co).<br>

## Configuration

    ./config
    
The configuration script parses *server.cfg* to get the server context, it installs the Python enviroment and generate SystemD services files.

## Installation

    ./config install
    
Install command needs root privileges and it basically puts the SysD files in /etc/systemd.

## Unistall

Remove the gunicorn*.service and web_artgallery from /etc/systemd/system and /etc/nginx/available-sites/ respectively.

## Project Elements

    .
    ├── about
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── templates
    │   │   └── about.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── artgallery
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── artwork
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── templates
    │   │   └── artwork.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── author
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── templates
    │   │   └── author.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── bash
    │   ├── dependencias.sh
    │   └── sync_db.sh
    ├── collection
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── templates
    │   │   └── collection.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── config
    ├── contact
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── templates
    │   │   └── contact.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── main
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── templates
    │   │   └── index.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── server.cfg
    └── template
        ├── assets
        │   ├── css
        │   ├── fonts
        │   └── js
        ├── base.html
        ├── elements.html
        ├── generic.html
        ├── images
        └── index_base.html
