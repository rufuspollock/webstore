
DEBUG = True
SECRET = 'foobar'

SQLITE_DIR = '/tmp'

AUTHORIZATION = {
    'self': ['read', 'write', 'delete'],
    'user': ['read'],
    'world': ['read']
    }

AUTH_FUNCTION = 'always_login'
HAS_FUNCTION = 'default'
AUTH_FUNCTION = 'always_login'
#CKAN_DB_URI = 'postgresql://okfn@localhost/ckantest'
