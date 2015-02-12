#!/Users/fcarrizalest/virtual/pyPlus/bin/python
from flup.server.fcgi import WSGIServer
from pyPlus import application

WSGIServer(application).run()
