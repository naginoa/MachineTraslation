import os
import requests
import random
from bs4 import BeautifulSoup


def getHTMLText(url):
    kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    proxy_list = [
        'http://119.90.126.106:7777',
        'http://101.89.132.131:80',
        'http://115.171.202.213:9000',
        'http://218.60.8.98:3129',
        'http://183.196.168.194:9000',
        'http://113.200.214.164:9999',
        'http://113.200.214.164:9999',
    ]
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    try:
        r = requests.get(url, headers=kv, proxies=proxies, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        print("Get HTML Text Failed!")
        return 0


#将文本拆成逐行
def getText(string):
    list = string.split('\n')
    list = [item + '\n' for item in list if item != '']

    return list


def google_translate_EtoC(to_translate, from_language="en", to_language="ch-CN"):
    # 根据参数生产提交的网址
    base_url = "https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, to_translate)

    # 获取网页
    html = getHTMLText(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")

    # 解析网页得到翻译结果
    try:
        result = soup.find_all("div", {"class": "t0"})[0].text
    except:
        print("Translation Failed!")
        result = ""

    return result


def google_translate_CtoE(to_translate, from_language="en", to_language="ch-CN"):
    # 根据参数生产提交的网址
    base_url = "https://translate.google.cn/m?hl={}&sl={}&ie=UTF-8&q={}"
    url = base_url.format(to_language, from_language, to_translate)

    # 获取网页
    html = getHTMLText(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")

    # 解析网页得到翻译结果
    try:
        result = soup.find_all("div", {"class": "t0"})[0].text
    except:
        print("Translation Failed!")
        result = ""

    #result_list = re.split('！|。|？', result)
    #print(result_list)
    #result_list = [item for item in filter(lambda x: x != '', result_list)]

    return result


def batch_trans(splitpath, transpath):
    folder_dir_list = os.listdir(splitpath)
    for f in folder_dir_list:
        file_list = os.listdir(splitpath + f)
        if not os.path.exists(transpath + f):
            os.mkdir(transpath + f)
        i = 0
        while (i <= len(file_list) - 2):
            if '@eng' in file_list[i].lower():
                en = file_list[i]
                zh = file_list[i + 1]
            elif '@eng' in file_list[i+1].lower():
                en = file_list[i + 1]
                zh = file_list[i]
            elif 'chi' in file_list[i].lower() or '译' in file_list[i].lower() or '中' in file_list[i].lower():
                en = file_list[i + 1]
                zh = file_list[i]
            elif 'chi' in file_list[i+1].lower() or '译' in file_list[i+1].lower() or '中' in file_list[i+1].lower():
                en = file_list[i]
                zh = file_list[i + 1]

            #print(splitpath + f + '/' + en)

            trans_lines = []
            with open(splitpath + f + '/' + en, encoding='utf-8') as f1:
                file_str = f1.read()
                for substr in getText(file_str):
                    print(google_translate_CtoE(substr))
                    trans_lines.append(google_translate_CtoE(substr))

            trans_title = en[:-4] + '@tran' + en[-4:]
            print(transpath + f + '/' + trans_title)
            with open(transpath + f + '/' + trans_title, 'w', encoding='utf-8') as f2:
                for line in trans_lines:
                    f2.write(line + '\n')

            i += 2


splitpath = 'D:/split/'
transpath = 'D:/translation/'
batch_trans(splitpath, transpath)


'''flag = 0
for i in getText(sss):
    #print(flag)
    flag += 1
    print(google_translate_CtoE(i))

print(flag)'''