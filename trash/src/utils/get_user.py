

from fastapi import Request
from src.utils.date_work import today



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

    return user