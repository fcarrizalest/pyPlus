#!/home/fcarrizalest/virtual/pyplus/bin/python
import sys
import logging

activate_this = '/home/fcarrizalest/virtual/pyplus/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/pyPlus/")

from pyPlus import app as application
