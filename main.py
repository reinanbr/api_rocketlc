
import uvicorn
from fastapi import FastAPI,Request
import datetime as dt
import time
import os
import rocketlc.space_schedulle_launch as sll
from db_sql import insert_user,get_users

def today():
    now = dt.datetime.now()
    hour = now.strftime('%H:%M:%S')
    date = now.strftime('%d/%m/%Y')
    return {'hour':hour,'date':date}


def get_user(client:Request.headers) -> dict:
    tdy = today()
    user = {'ip':client.get('host'),
            'userAgent':client.get('user-agent'),
            'lang':client.get("accept-language"),
            'mode':client.get("sec-fetch-mode"),
            'platform':client.get("sec-ch-ua-platform"),
            'navigator':client.get("sec-ch-ua"),
            'date':tdy['date'],
            'hour':tdy['hour']
            }
            # 'userAgent':client.get('user-agent'),
            # 'accept':client.get('accept'),
            # 'mobile':client.get("sec-ch-ua-mobile"),
            # 'lang':client.get("accept-language"),
            # 'mode':client.get("sec-fetch-mode"),
            # 'app':client.get("sec-ch-ua"),
            # 'dest':client.get("sec-fetch-dest"),
            # 'isUser':client.get("sec-fetch-user"),
            # 'platform':client.get("sec-ch-ua-platform"),
            # 'insecureRequests':client.get("upgrade-insecure-requests"),
            # 'site':client.get("sec-fetch-site")}
    
    return user


app = FastAPI(debug=True)

@app.get('/')
async def start(request:Request):
    client = request.headers
    print(client)
    return get_user(client)



@app.get('/users')
async def users_():
    data_users = {}
    for usr in get_users():
        data_users[usr[1]] = {'headers':usr[2],'last_date':usr[3],'last_hour':usr[4],'count_acess':usr[5]}
    return data_users



@app.get('/ssl')
async def ssl(request:Request):
    user_info = get_user(request.headers)
    data_lauch = sll.launchs()
    insert_user(user_info)
    
    return {'data':data_lauch,'user_info':user_info}
# @app.get('/search/bg/{query}')
# def bg(query:str,page_limit:int,request:Request):
#     ping_init = time.time()
#     res_bg = sb.search_porn(query,page_limit)
#     ping_end = time.time() - ping_init
#     client = request.headers

#     data = {}
#     data['user'] = get_user(client)
#     data['site'] = 'SpankBang'
#     data['len_results'] = len(res_bg)
#     data['ping'] = ping_end
#     data['links'] = res_bg
   
#     return data


# @app.get('/pesq/{q}')
# def pesq(q:str,n:int=10,lg:str='en'):
#     return search(term=q,num_results=n,lang=lg)

# @app.get('/yt/{m}')
# def get_music(m:str):
#     lyt = gm(m)
#     return lyt

#uvicorn.run(app,host='0.0.0.0',port=8000)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run('main:app', host="0.0.0.0", port=port, reload=True)