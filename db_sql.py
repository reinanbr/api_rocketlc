import sqlite3

db_users = sqlite3.connect('db/users.db')
db_users_cursor = db_users.cursor()


def insert_user(user:dict)-> dict:
    
    db_users_cursor.execute(f'')
    

def get_users():
    return db_users_cursor.execute('select * from users').fetchall()

def filter_user_ip(ip:str):
    return db_users_cursor.execute(f"select ip from users where ip='{ip}'").fetchall()