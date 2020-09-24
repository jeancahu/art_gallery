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
.<br>
├── about<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── templates<br>
│   │   └── about.html<br>
│   ├── tests.py<br>
│   ├── urls.py<br>
│   └── views.py<br>
├── artgallery<br>
│   ├── asgi.py<br>
│   ├── settings.py<br>
│   ├── urls.py<br>
│   └── wsgi.py<br>
├── artwork<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── templates<br>
│   │   └── artwork.html<br>
│   ├── tests.py<br>
│   ├── urls.py<br>
│   └── views.py<br>
├── author<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── templates<br>
│   │   └── author.html<br>
│   ├── tests.py<br>
│   ├── urls.py<br>
│   └── views.py<br>
├── bash<br>
│   ├── dependencias.sh<br>
│   └── sync_db.sh<br>
├── collection<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── templates<br>
│   │   └── collection.html<br>
│   ├── tests.py<br>
│   ├── urls.py<br>
│   └── views.py<br>
├── config<br>
├── contact<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── templates<br>
│   │   └── contact.html<br>
│   ├── tests.py<br>
│   ├── urls.py<br>
│   └── views.py<br>
├── main<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── templates<br>
│   │   └── index.html<br>
│   ├── tests.py<br>
│   ├── urls.py<br>
│   └── views.py<br>
├── server.cfg<br>
└── template<br>
    ├── assets<br>
    │   ├── css<br>
    │   ├── fonts<br>
    │   └── js<br>
    ├── base.html<br>
    ├── elements.html<br>
    ├── generic.html<br>
    ├── images<br>
    └── index_base.html<br>
