from .base import *
import logging

NPLUSONE = True

# NPLUSONE
NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

INSTALLED_APPS.append('nplusone.ext.django')

MIDDLEWARE.append('nplusone.ext.django.NPlusOneMiddleware')
