#-*- coding:utf-8 -*-
import sys

# Expand Python classes path with your app's path
sys.path.insert(0, "C:\Apache24\Test_web\www")

from mainapp import app

# Put logging code (and imports) here ...

# Initialize WSGI app object
application = app
