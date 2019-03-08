import requests


kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36'
                    ' (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
try:
    requests.get('http://www.baidu.com/', headers=kv, proxies={"http": "http://122.136.212.132:53281"})
except:
    print('connect failed')
else:
    print('success')