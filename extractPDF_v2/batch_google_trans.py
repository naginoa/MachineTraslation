import os
import requests
import random
from bs4 import BeautifulSoup


def getHTMLText(url):
    kv = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    proxy_list = [
        'http://124.192.106.247:3128',
        'http://121.69.10.62:9090',
        'http://14.29.2.40:80',
        'http://31.131.67.14:8080',
        'http://103.61.153.100:53281',
        'http://117.158.57.2:3128',
        'http://101.89.91.147:80',
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


# 将文本拆成逐行
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

    # result_list = re.split('！|。|？', result)
    # print(result_list)
    # result_list = [item for item in filter(lambda x: x != '', result_list)]

    return result


def batch_trans(splitpath, transpath):
    folder_dir_list = os.listdir(splitpath)
    for f in folder_dir_list:
        file_list = os.listdir(splitpath + f)
        if not os.path.exists(transpath + f):
            os.mkdir(transpath + f)
        index = 0

        while index <= len(file_list) - 2:
            for_fn = file_list[index]
            lat_fn = file_list[index + 1]
            # each_store_para(rootpath + f + '/' + file, storepath + f + '/')
            if for_fn.rsplit('.', 2)[0] == lat_fn.rsplit('.', 2)[0]:
                # print(for_fn, lat_fn)
                en_fn = for_fn if '.en' in for_fn.lower() else lat_fn
                zh_fn = for_fn if '.zh' in for_fn.lower() else lat_fn
                print(en_fn, zh_fn)
                index += 1

                trans_lines = []
                with open(splitpath + f + '/' + en_fn, encoding='utf-8') as f1:
                    file_str = f1.read()
                    for substr in getText(file_str):
                        print(google_translate_CtoE(substr))
                        trans_lines.append(google_translate_CtoE(substr))

                trans_title = en_fn.replace('.en', '.tran')
                print(transpath + f + '/' + trans_title)
                with open(transpath + f + '/' + trans_title, 'w', encoding='utf-8') as f2:
                    for line in trans_lines:
                        f2.write(line + '\n')

            index += 1


if __name__ == "__main__":
    splitpath = 'D:/v2_extract/split/'
    transpath = 'D:/v2_extract/translation/'
    batch_trans(splitpath, transpath)