import re
import os


filename = 'zh.txt'
endchar = '。'


def zh_split_each_sentence(senpath, splitpath):
    with open(senpath, encoding='utf-8') as f:
        #add .
        for line in f.readlines():
            newline = ''
            if len(line) == 1:
                continue
            if line.strip().endswith(endchar):
                newline = line.strip()
            else:
                newline = line.strip() + endchar

            if newline.count(endchar) > 1:
                #sublinelist = [i + endchar for i in newline.split(endchar)[:-1]]
                sublinelist = re.split('！|。|？', newline)
                sublinelist = [item + endchar for item in filter(lambda x: x != '', sublinelist)]
                #print(sublinelist)
                print(splitpath + senpath.split('/')[-1])
                with open(splitpath + senpath.split('/')[-1], 'a', encoding='utf-8') as f:
                    for i in sublinelist:
                        f.write(i + '\n')
            else:
                with open(splitpath + senpath.split('/')[-1], 'a', encoding='utf-8') as f:
                    f.write(newline + '\n')


def zh_batch_split(senpath, splitpath):
    folder_dir_list = os.listdir(senpath)
    for f in folder_dir_list:
        if not os.path.exists(splitpath + f):
            os.mkdir(splitpath + f)
        file_list = os.listdir(senpath + f)
        for file in file_list:
            print(senpath + f + '/' + file)
            zh_split_each_sentence(senpath + f + '/' + file, splitpath + f + '/')



'''with open(filename, encoding='utf-8') as f:
    #add .
    for line in f.readlines():
        newline = ''
        if len(line) == 1:
            continue
        if line.strip().endswith(endchar):
            newline = line.strip()
        else:
            newline = line.strip() + endchar

        if newline.count(endchar) > 1:
            sublinelist = [i + endchar for i in newline.split(endchar)[:-1]]
            #print(sublinelist)
            with open('zh_split.txt', 'a', encoding='utf-8') as f:
                for i in sublinelist:
                    f.write(i + '\n')
        else:
            with open('zh_split.txt', 'a', encoding='utf-8') as f:
                f.write(newline + '\n')
'''