# 首先导入需要的包
from googletrans import Translator
from tqdm import tqdm
import os
import random
import time


# 声明源文件目录 和 生成文件的放置目录
home = 'D:/'
path = home + "/transtest/"
dest = home + "/transtest2/"
files = os.listdir(path)
s = []


# 把长文本切分成短文本，当时google担心会检查文本长度，所以随机了长度，应该没这么严格，想写成固定的也可以
'''def getText(string):
    list = []
    randline = 1
    #randline = random.random() * 500 
    while len(string) > 1500:
        index = string.find("\n", int(randline) + 1000)
        if index is not None:
            list.append(string[0:index])
            string = string[index:]
    list.append(string)
    return list
'''


def getText(string):
    list = [line + '\n' for line in string.split('\n')]
    return list


# 保存翻译完后的文件
def save2file(title, result):
    with open(dest + "/" + title, 'w', encoding='utf-8') as d:
        for en in result:
            d.write(en)
        d.close


# 打印单个文本分段后的翻译进度
def printProcess(cnt, txt_len, tatal_size, error):
    content = "file completed " + str(cnt) + "/" + str(txt_len)
    print(content, end="\r")


# 在短文本翻译出错后，用二分法找到错误地方，并舍去无法翻译的句子
def binarySearch(text):
    mid = (int)(len(text) * 1.0 / 2)
    result = []
    splitIndex = text.find("。", mid)
    if splitIndex == -1 or splitIndex == 0:
        return result

    pre = text[0:splitIndex]
    after = text[splitIndex + 1:]
    try:
        result = result + append(pre)
    except:
        result = result + binarySearch(pre)

    try:
        result = result + append(after)
    except:
        result = result + binarySearch(after)

    return result


# 翻译文本
def getTranslateTextList(txt):
    result = []
    time.sleep(1)
    cnt = 0
    txtsize = 0

    for text in txt:
        try:
            cnt += 1
            txtsize += len(text)
            translate = Translator(service_urls=['translate.google.cn'])
            en = translate.translate(text=text, dest='zh-CN').text
            result.append(en + '\n')
            printProcess(cnt, len(txt), txtsize, error)
            slptimes = random.random()  # 我可能想太多，怕固定的sleep还是会被google检查出来，所以随机了一个时间
            time.sleep(1.2 + slptimes)
        except Exception as e:
            result = result + binarySearch(text)
    return result


for file in tqdm(files):
    if not os.path.isdir(file):
        title = file
        try:
            with open(path + "/" + file, 'r', encoding='utf-8') as f:
                string = f.read()
                f.close()
            txt = getText(string)
            print("analysis:" + title)
            result = getTranslateTextList(txt)
            save2file(title, result)
        except Exception as e:
            print(str(e))
            continue
    time.sleep(10)  # 为了保证不被google屏蔽IP，不得已设置了一个超长时间的sleep，可以按情况改小
