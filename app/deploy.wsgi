import os
import sys
import site

# Add virtualenv site packages
site.addsitedir(os.path.join(os.path.dirname(__file__), 'venv/lib/site-packages'))

# Path of execution
sys.path.append('flaskapp')

# Fired up virtualenv before include application
activate_env = os.path.expanduser(os.path.join(os.path.dirname(__file__), 'venv/Scripts/activate_this.py'))
execfile(activate, dict(__file__=activate))

# import my_flask_app as application
from deploy import app as application
