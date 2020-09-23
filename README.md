# Art Gallery

Django backend<br>
Nginx web server<br>
Spatial by [TEMPLATED](https://templated.co)<br>

## Configuration

    ./config
    
The configuration script parses *server.cfg* to get the server context, it installs the Python enviroment and generate SystemD services files.

    ./config install
    
Install command needs root privileges and it basically puts the SysD files in /etc/systemd
