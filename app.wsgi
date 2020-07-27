#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/PiApi/")

from PiApi import app as application

from werkzeug.debug import DebuggedApplication

application.secret_key = 'skdjh54fsk4rw54djsdxcf6'

a = DebuggedApplication(application, evalex=True)

