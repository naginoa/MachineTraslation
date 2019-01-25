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


root_dir = 'D:/experdata/'
folder_dir_list = os.listdir(root_dir)
for f in folder_dir_list:
    #print(f, len(os.listdir(root_dir + f)))
    file_list = os.listdir(root_dir + f)
    print(f, len(file_list))

    not_ppt_list = [i for i in file_list if '.ppt' not in str(i)]
    print(f, len(not_ppt_list))

    ppt_list = [i for i in file_list if '.ppt' in str(i)]
    print(ppt_list)



f2 = open('D:/pickle/dump.txt', 'rb')
d = pickle.load(f2)
f2.close()
print(d)

print(string.punctuation)
print(count_punc('The weight of each strip (10 vials) should be 12.5 ± 2 g.'))
print(len('The weight of each strip (10 vials) should be 12.5 ± 2 g.'))
print(count_punc('The weight of each strip (10 vials) should be 12.5 ± 2 g.') < 0.3*len('The weight of each strip (10 vials) should be 12.5 ± 2 g.'))
print(count_punc('___________    ______'))
print(len('___________    ______'))
print(count_punc('___________    ______') < 0.3 * len('___________    ______'))

print(is_number('dasdsa'))