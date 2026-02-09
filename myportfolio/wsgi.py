import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")

# Standard Django WSGI application
application = get_wsgi_application()

# This line makes it work on Vercel
app = application