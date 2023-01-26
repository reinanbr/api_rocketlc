import os
import json

FILE_DB = '/tmp/users_db.json'

if not os.path.isfile(FILE_DB):
    os.system(f'cp users_db.json {FILE_DB}')


def read_db():
    file = open(FILE_DB)
    data_db = json.load(file)
    return data_db
    

def add_acess(user:dict):
    db = read_db()
    acess = db['acess']
    acess.append({"ip":user['ip'],'userAgent':user['userAgent'],"date":user['date'],"hour":user['hour']})
    db['acess'] = acess
    new_data_db = json.dumps(db,indent=4)
    with open(FILE_DB,'w') as file:
        file.write(new_data_db)


def filter_acess(ip):
    db = read_db()
    acess = db['acess']
    acess_list_ip = []
    for acss in acess:
        if acss['ip'] == ip:
            acess_list_ip.append(acss)
    return acess_list_ip

def add_user(user:dict):
    add_acess(user)
    count_acess = len(filter_acess(user['ip']))

    db = read_db()
    users = db['users']
    usr_base = 0
    i = 0
    for usr in users:
        if user['ip']==usr['ip']:
            usr['lastDate'] = user['date']
            usr['lastHour'] = user['hour']
            usr['countAcess'] = count_acess
            usr_base = usr
            users[i] = usr_base
        i = i+1
    if not usr_base:
        usr = {}
        usr['lastDate'] = user['date']
        usr['lastHour'] = user['hour']
        usr['ip'] = user['ip']
        usr['userAgent'] = user['userAgent']
        usr['countAcess'] = count_acess
        users.append(usr)
    db['users'] = users
    new_data = json.dumps(db,indent=4)
    with open(FILE_DB,'w') as file:
        file.write(new_data)
            