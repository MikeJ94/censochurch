import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3'),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'postgre',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbcenso',
        'USER': 'root',
        'PASSWORD': 'Abc.123',
        'HOST': 'localhost',
        'PORT': '3306'

    }
}