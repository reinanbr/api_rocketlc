import sqlite3



def insert_acess(user):
    
    db_users = sqlite3.connect('db/users.db')
    db_users_cursor = db_users.cursor()
    
    command = f"insert into acess(ip,date,hour,userAgent) values('{user['ip']}','{user['date']}','{user['hour']}','{user['userAgent']}')"
    db_users_cursor.execute(command)
    
    
    db_users.commit()
  #  db_users_cursor.close()
    db_users.close()
        
    
    




def get_acess_ip(ip):
    
    db_users = sqlite3.connect('db/users.db')
    db_users_cursor = db_users.cursor()
    
    res = db_users_cursor.execute(f"select ip,date,hour from acess where ip='{ip}'").fetchall()
    
    
    db_users.commit()
  #  db_users_cursor.close()
    db_users.close()
        
    
    return res


def insert_user(user:dict)-> dict:
    db_users = sqlite3.connect('db/users.db')
    db_users_cursor = db_users.cursor()
    
    insert_acess(user)
    acess = get_acess_ip(user['ip'])
    
    command = f"insert into users(ip,headers,last_date,last_hour,count_acess) values('{user['ip']}','{user['userAgent']}','{user['date']}','{user['hour']}',{len(acess)})"
    print(command)
    usr = filter_user_ip(user['ip'])
    print(usr)
    if usr:
        if not user['ip'] in usr[0]:
            print('first time')
            db_users_cursor.execute(command)
            
        else:
            print('olá dnv')
            command = f"update users set last_hour='{user['hour']}' where ip='{user['ip']}'" # count_acess={len(acess)}
            db_users_cursor.execute(command)
            db_users_cursor.execute(f"update users set last_date='{user['date']}' where ip='{user['ip']}'")
            db_users_cursor.execute(f"update users set count_acess={len(acess)} where ip='{user['ip']}'")
    db_users.commit()
  #  db_users_cursor.close()
    db_users.close()
        
    

def get_users():
    
    db_users = sqlite3.connect('db/users.db')
    db_users_cursor = db_users.cursor()
    
    res = db_users_cursor.execute('select * from users').fetchall()
    
    db_users.commit()
  #  db_users_cursor.close()
    db_users.close()
        
    return res

def filter_user_ip(ip:str):
    
    db_users = sqlite3.connect('db/users.db')
    db_users_cursor = db_users.cursor()
    
    res = db_users_cursor.execute(f"select ip from users where ip='{ip}'").fetchall()
    
    
    db_users.commit()
  #  db_users_cursor.close()
    db_users.close()
        
    
    return res

