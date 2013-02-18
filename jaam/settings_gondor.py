import os
import dj_database_url

from .settings import *

DATABASES = {
    "default": dj_database_url.config(env="GONDOR_DATABASE_URL"),
}

# this is overridden by gondor
GONDOR_DATA_DIR = os.environ['GONDOR_DATA_DIR']

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
