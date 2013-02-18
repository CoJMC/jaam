import os
import dj_database_url

from .settings import *

DATABASES = {
    "default": dj_database_url.config(env="GONDOR_DATABASE_URL"),
}

# this is overridden by gondor
GONDOR_DATA_DIR = os.environ['GONDOR_DATA_DIR']

MEDIA_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "media")
STATIC_ROOT = os.path.join(os.environ["GONDOR_DATA_DIR"], "site_media", "static")

MEDIA_URL = "/s/media/" # make sure this maps inside of site_media_url
STATIC_URL = "/s/static/" # make sure this maps inside of site_media_url
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, "admin" + os.path.sep)

# Whoosh Search Engine
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(GONDOR_DATA_DIR, "whoosh_index"),
        'STORAGE': 'file',
        'INCLUDE_SPELLING': True,

    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5
