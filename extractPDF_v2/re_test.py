import re
import os


filename = 'zh.txt'
endchar = '。'
s = '。！？'

#def batch_spilt_sentences(rootpath, storepath):
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


#print('D:/test/200801/Encrypted ProTime译稿.txt'.split('.'))
zh_split_each_sentence('D:/test/200801/Encrypted ProTime译稿.txt', 'D:/')


s = '。！？'

string = '在人肝细胞制备！物H0088中LY450139？对睾酮6β-羟基化酶活性的影响。'

l = re.split('！|。|？', string)
l = [item for item in filter(lambda x:x != '', l)]
print(l)