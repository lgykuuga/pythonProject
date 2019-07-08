import requests
import itchat
import json
import datetime
import time


city = '深圳'
url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city

def get_weather():
    resp = requests.get(url)
    return json.loads(resp.text)

def send_data(data):
    print(data)
    friends = itchat.search_friends(name = '黄莹莹')
    print(friends)
    username = friends[0]['UserName']
    data = data['date'] + ' ' + data['type'] + ' ' + data['high'] + ' ' + data['low']
    itchat.send(data, toUserName=username)
    print(data)


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    while True:
        time_now = datetime.datetime.now()
        if time_now.hour == 16 and time_now.minute == 37:
            data = get_weather()
            data = data['data']['forecast'][0]
            send_data(data)
            time.sleep(60)
        else:
            time.sleep(60)
            print('waiting')
    
