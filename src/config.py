SECRET_KEY = "NULL"
CSRF_ENABLED = True

from os import getcwd, path

BASE_DIR = getcwd()

UPLOAD_DIR      = BASE_DIR + '/src/uploads'
TEMPLATE_DIR    = BASE_DIR + '/src/templates'
DATABASE_DIR    = BASE_DIR + '/src/database'
