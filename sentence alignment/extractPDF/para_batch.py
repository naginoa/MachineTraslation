from docx import Document
import os
import pickle
import string


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


#计算句子中符号个数
def count_punc(st):
    flag = 0
    for s in st:
        if s in string.punctuation:
            flag += 1

    return flag


#一次读取一个文件
def each_store_para(pdfpath, storepath):
    pdfname = pdfpath.split('/')[-1][:-5]
    document = Document(pdfpath)
    ps = document.paragraphs
    texts = []

    for p in ps:
        #过滤空格 and 符号过多的句子 and 纯数字
        if len(p.text) > 1 and count_punc(p.text) < 0.3 * len(p.text) and not is_number(p.text.strip().strip('.')):
            texts.append(p.text.strip().strip('.'))

    # 去重并保持顺序
    no_repe_texts = list(set(texts))
    no_repe_texts.sort(key=texts.index)
    with open(storepath + pdfname + '.txt', 'a', encoding='utf-8') as f:
        for t in no_repe_texts:
            print(t)
            f.write(t + '\n')


def batch_store_para(rootpath, storepath):
    f2 = open('D:/pickle/dump.txt', 'rb')
    pickle_dict = pickle.load(f2)
    f2.close()
    for i in pickle_dict.keys():
        for p in pickle_dict[i]:
            #print(p[0], p[1])
            if '.pdf' in p[0].lower():
                for file in os.listdir(rootpath + i):
                    if file[:-9] == p[0][:-4]:
                        print(rootpath + i + '/' + file)
                        each_store_para(rootpath + i + '/' + file, storepath + i + '/')
                    if file[:-5] == p[1][:-4]:
                        print(rootpath + i + '/' + file)
                        each_store_para(rootpath + i + '/' + file, storepath + i + '/')
            else:
                for file in os.listdir(rootpath + i):
                    if file[:-5] == p[0][:-4]:
                        print(rootpath + i + '/' + file)
                        each_store_para(rootpath + i + '/' + file, storepath + i + '/')
                    if file[:-5] == p[1][:-4]:
                        print(rootpath + i + '/' + file)
                        each_store_para(rootpath + i + '/' + file, storepath + i + '/')


rootpath = 'D:/cooked_data/'
storepath = 'D:/test/'
#each_store_para(rootpath + '200801/' + '08- formulation of DP@eng.docx', storepath)
batch_store_para(rootpath, storepath)