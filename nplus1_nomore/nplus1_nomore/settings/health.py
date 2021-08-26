from .base import *

HEALTH = True

INSTALLED_APPS = INSTALLED_APPS + [
    'health_check',                             
    'health_check.db',                          
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',
    ]
