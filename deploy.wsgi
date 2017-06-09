import os
import sys
import site

# Add virtualenv site packages
site.addsitedir(os.path.join(os.path.dirname(__file__), '/var/www/flaskapp/venv/Lib/site-packages'))
# Path of execution
sys.path.append('/var/www/flaskapp/app')

# Fired up virtualenv before include application
activate_this = '/var/www/flaskapp/venv/Scripts/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# import my_flask_app as application
from app import app as application

