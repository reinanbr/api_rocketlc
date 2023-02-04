
import uvicorn
from fastapi import FastAPI,Request
import datetime as dt
import time
import os
import rocketlc.space_schedulle_launch as sll
# from db_sql import insert_user,get_users
from db_json import read_db,add_user,add_acess
from fastapi.middleware.cors import CORSMiddleware


def today():
    now = dt.datetime.now()
    hour = now.strftime('%H:%M:%S')
    date = now.strftime('%d/%m/%Y')
    return {'hour':hour,'date':date}


def get_user(client:Request) -> dict:
    tdy = today()
    c = client
    cli = client.client
    client = client.headers
    user = {'ip':cli[0],#get('adress'),
            'userAgent':client.get('user-agent'),
            'lang':client.get("accept-language"),
            'mode':client.get("sec-fetch-mode"),
            'platform':client.get("sec-ch-ua-platform"),
            'navigator':client.get("sec-ch-ua"),
            'date':tdy['date'],
            'hour':tdy['hour'],
            'url':c.url._url
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
    print(user)
    return user


app = FastAPI(debug=True)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/',tags=["Root"])
async def start(request:Request):
    add_user(get_user(request))
    client = request.url
    print(client)
    get_user(request)
    return client # get_user(client)



@app.get('/db')
async def users_(request:Request):
    add_user(get_user(request))
    return read_db()



@app.get('/ssl')
async def ssl(request:Request):

    add_user(get_user(request))
    data_lauch = sll.launchs()

    
    return {
    'statusCode': 200,
    'headers': {
  "Access-Control-Allow-Origin": "*", #Required for CORS support to work
  "Access-Control-Allow-Credentials": True, #// Required for cookies, authorization headers with HTTPS
  "Access-Control-Allow-Headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
  "Access-Control-Allow-Methods": "POST, OPTIONS"
},'body':data_lauch}
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