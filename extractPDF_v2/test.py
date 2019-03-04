import os
import string
import random
import numpy as np
from scipy.linalg import norm
from sklearn.feature_extraction.text import CountVectorizer


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


def count_punc(st):
    flag = 0
    for s in st:
        if s in string.punctuation:
            flag += 1

    return flag


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""

    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':

        return True

    else:

        return False


def getText(string):
    list = []
    randline = random.random() * 500
    while len(string) > 1500:
        index = string.find("\n", int(randline) + 1000)
        if index is not None:
            list.append(string[0:index])
            string = string[index:]
    list.append(string)
    return list


def tf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


if __name__ == "__main__":
    s1 = 'AneuVysion IUO Customer Training'
    s2 = 'AneuVysion IUO客户培训'
    splitpath = 'D:/v2_extract/translation/'
    if s1 in s2 or s2 in s1 or tf_similarity(s1, s2) >= 0.82:
        print('yes')
    else:
        print('no')

    # print(tf_similarity(s1, s2))

    folder_dir_list = os.listdir(splitpath)
    for f in folder_dir_list:
        file_list = os.listdir(splitpath + f)
        for fi in file_list:
            os.rename(splitpath + f + '/' + fi, splitpath + f + '/' + fi.replace('.en', '.tran'))
