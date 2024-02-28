import datetime as dt
import time
import os


def today():
    now = dt.datetime.now()
    hour = now.strftime('%H:%M:%S')
    date = now.strftime('%d/%m/%Y')
    return {'hour':hour,'date':date}


