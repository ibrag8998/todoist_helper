import os

from . import api_token


API_TOKEN = api_token.API_TOKEN # calambur
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKUP_FILE = os.path.join(BASE_DIR, 'backup.txt')
