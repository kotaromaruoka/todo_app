import requests
import datetime
import os
from dotenv import load_dotenv
import time

load_dotenv()

push_time = input('time? ')
message = input('message? ')

while True:
    print('loop')
    now = datetime.datetime.now()
    day = now.strftime('%Y-%m-%d')
    print(day)
    print(now)
    #push_time = datetime.datetime.strptime(day + ' 10:57:00', '%Y-%m-%d %H:%M:%S')
    print(push_time)
    push_datetime = day + ' ' + push_time
    print(str(now)[0:16])
    print(str(push_time)[0:16] == str(now)[0:16])
    if str(push_datetime)[0:16] == str(now)[0:16]:
        print('push')
        url = "https://notify-api.line.me/api/notify"
        access_token = os.environ["LINE_TOKEN"]
        headers = {"Authorization": "Bearer " + access_token}
        payload = {"message": 'hello'}
        r = requests.post(url,headers=headers,params=payload,)
        
    time.sleep(60)