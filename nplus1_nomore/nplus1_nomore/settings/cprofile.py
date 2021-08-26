from .base import *

CPROFILE = True

DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF = False
MIDDLEWARE.append('django_cprofile_middleware.middleware.ProfilerMiddleware',)
