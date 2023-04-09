import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from utils import get_file_path

def db_init():
    DB_PATH = get_file_path('db/bank_holidays.db')
    DB_URL = 'sqlite:///' + DB_PATH

    print(DB_URL)

    engine = create_engine(DB_URL)
    return engine;

def print_tables(engine):
    print('Table info')
    inspector = inspect(engine)
    print(inspector.get_table_names())

