from os import environ, path
from utils import get_file_path
from dotenv import load_dotenv

load_dotenv(get_file_path('.env'))

TESTING = 'Bing!'

def get_config(key):
    return environ.get(key)
