from .base import *

SILK = True

# SILK
SILKY_PYTHON_PROFILER = True

MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

INSTALLED_APPS.append('silk')
