import os
import shutil
import numpy as np
from scipy.linalg import norm
from sklearn.feature_extraction.text import CountVectorizer


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


def get_pairs_dict(oripath):
    folder_dir_list = os.listdir(oripath)
    pairs_dict = {}

    for f in folder_dir_list:
        pairs_dict.update({f: []})
        file_list = os.listdir(oripath + f)
        i = 0

        while i <= len(file_list) - 2:
            former_fn = file_list[i].rsplit('.', 1)[0]
            latter_fn = file_list[i + 1].rsplit('.', 1)[0]
            # 判断句子是否为一对

            if former_fn in latter_fn or latter_fn in former_fn or tf_similarity(former_fn, latter_fn) >= 0.82:
                # 判断哪个为译文(中文)并过滤掉两对都是译文的情况

                if 'chi' in former_fn.lower() or '译' in former_fn.lower() or '中' in former_fn.lower():
                    if '译' not in latter_fn.lower() and 'chi' not in latter_fn.lower() and '中' not in latter_fn.lower():
                        former_suf = file_list[i].rsplit('.', 1)[1]
                        latter_suf = file_list[i + 1].rsplit('.', 1)[1]
                        # 要么两个都是PPT，要么两个都不是PPT
                        if (former_suf + latter_suf).lower() != 'pptppt':
                            if former_suf != 'ppt' and latter_suf != 'ppt':
                                sublist = [file_list[i + 1], file_list[i]]
                                pairs_dict[f].append(sublist)
                                i += 1
                        else:
                            sublist = [file_list[i + 1], file_list[i]]
                            pairs_dict[f].append(sublist)
                            i += 1

                elif 'chi' in latter_fn.lower() or '译' in latter_fn.lower() or '中' in latter_fn.lower():
                    if '译' not in former_fn.lower() and 'chi' not in former_fn.lower() and '中' not in former_fn.lower():
                        former_suf = file_list[i].rsplit('.', 1)[1]
                        latter_suf = file_list[i + 1].rsplit('.', 1)[1]
                        # 要么两个都是PPT，要么两个都不是PPT
                        if (former_suf + latter_suf).lower() != 'pptppt':
                            if former_suf != 'ppt' and latter_suf != 'ppt':
                                sublist = [file_list[i], file_list[i + 1]]
                                pairs_dict[f].append(sublist)
                                i += 1
                        else:
                            sublist = [file_list[i], file_list[i + 1]]
                            pairs_dict[f].append(sublist)
                            i += 1

                elif '.pdf' in file_list[i].lower() and '.doc' in file_list[i + 1]:
                    sublist = [file_list[i], file_list[i + 1]]
                    pairs_dict[f].append(sublist)
                    i += 1

                elif '.doc' in file_list[i] and '.pdf' in file_list[i + 1].lower():
                    sublist = [file_list[i + 1], file_list[i]]
                    pairs_dict[f].append(sublist)
                    i += 1

                else:
                    pass
                    # print('--------')
                    # print(no_ppt_list[i], no_ppt_list[i + 1])

            i += 1

        # print(f, (pairs_dict[f]))

    return pairs_dict


# 将配对好的文件重新载入到pairspath中，并重新命名以便后续操作。
def gen_pairs_folder(oripath, pairspath):
    pairs_dict = get_pairs_dict(oripath)
    for i in pairs_dict.keys():
        if not os.path.exists(pairspath + i):
            os.mkdir(pairspath + i)

        for p in pairs_dict[i]:
            # 取最后一个 . 的前边做文件名
            new_for_fn = p[0].rsplit('.', 1)[0] + '.en.' + p[0].rsplit('.', 1)[1]
            # 这里两个文件名的前缀都使用英文文档的名字命名表示配对
            new_lat_fn = p[0].rsplit('.', 1)[0] + '.zh.' + p[1].rsplit('.', 1)[1]
            print(new_for_fn, new_lat_fn)

            shutil.copyfile(oripath + i + '/' + p[0], pairspath + i + '/' + new_for_fn)
            shutil.copyfile(oripath + i + '/' + p[1], pairspath + i + '/' + new_lat_fn)


if __name__ == "__main__":
    oripath = 'D:/v2_extract/oridata/'
    pairspath = 'D:/v2_extract/pairs/'
    gen_pairs_folder(oripath, pairspath)