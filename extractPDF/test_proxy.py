import requests

try:
    requests.get('http://www.baidu.com/', proxies={"http":"http://124.205.155.146:9090"})
except:
    print('connect failed')
else:
    print('success')