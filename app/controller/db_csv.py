# тут будет модуль работы с CSV
import os
from app.model import tel
import sqlite3

conn = None
db_file_name = './import/tel.csv'
# file_name = './import/tel.csv'

def get_data_from_file(file_name=None):

    if file_name == None:
        return []
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            lst_str = f.read().splitlines()

        return [tuple(elem_str.split(',')) for elem_str in lst_str]
    except:
        return []


def get_data(str_pattern):
    print('CSV mode not supported yet')
    return []


def init():
    global conn
    if os.path.isfile(db_file_name):
        try:
            conn = sqlite3.connect(db_file_name)
        except:
            print('Error connecting to SQLite database')
    else:
        conn = sqlite3.connect(db_file_name)

    # create_table()
