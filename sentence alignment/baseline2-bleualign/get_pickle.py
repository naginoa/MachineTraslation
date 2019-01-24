import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm


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


def get_pairs_dict(root_dir):
    folder_dir_list = os.listdir(root_dir)
    pairs_dict = {}
    for f in folder_dir_list:
        #print(f, len(os.listdir(root_dir + f)))
        pairs_dict.update({f: []})
        file_list = os.listdir(root_dir + f)
        no_ppt_list = [g for g in file_list if '.ppt' not in str(g).lower()]
        #print(f, len(no_ppt_list))
        i = 0
        while (i <= len(no_ppt_list) - 2):
            pre = no_ppt_list[i][:-4]
            bak = no_ppt_list[i+1][:-4]
            #判断句子是否为一对
            #if pre in bak or bak in pre:
            if tf_similarity(pre, bak) >= 0.82:
                #print(1)
                if 'chi' in pre.lower() or '译' in pre.lower() or '中' in pre.lower():
                    sublist = [no_ppt_list[i + 1], no_ppt_list[i]]
                    pairs_dict[f].append(sublist)
                    i += 1
                    #print(sublist)
                elif 'chi' in bak.lower() or '译' in bak.lower() or '中' in bak.lower():
                    sublist = [no_ppt_list[i], no_ppt_list[i + 1]]
                    pairs_dict[f].append(sublist)
                    i += 1
                elif '.pdf' in no_ppt_list[i].lower() and '.doc' in no_ppt_list[i+1]:
                    sublist = [no_ppt_list[i], no_ppt_list[i + 1]]
                    pairs_dict[f].append(sublist)
                    i += 1
                elif '.doc' in no_ppt_list[i] and '.pdf' in no_ppt_list[i + 1].lower():
                    sublist = [no_ppt_list[i + 1], no_ppt_list[i]]
                    pairs_dict[f].append(sublist)
                    i += 1
                else:
                    pass
                    #print('--------')
                    #print(no_ppt_list[i], no_ppt_list[i + 1])

            i += 1

        #print(f, (pairs_dict[f]))

    return pairs_dict


root_dir = 'D:/experdata/'
pairs_dict = get_pairs_dict(root_dir)
with open('D:/pickle/' + 'dump.txt', 'wb') as f2:
    pickle.dumps(pairs_dict)
    pickle.dump(pairs_dict, f2)