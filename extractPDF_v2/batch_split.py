import os
from zh_split import zh_split_each_sentence
from en_split import en_split_each_sentence


def batch_split_files(textpath, splitpath):
    folder_dir_list = os.listdir(textpath)
    for f in folder_dir_list:
        file_list = os.listdir(textpath + f)

        if not os.path.exists(splitpath + f):
            os.mkdir(splitpath + f)

        index = 0
        while index <= len(file_list) - 1:
            fn = file_list[index]
            if fn.endswith('.zh'):
                print(textpath + f + '/' + fn, splitpath + f + '/')
                zh_split_each_sentence(textpath + f + '/' + fn, splitpath + f + '/')
            elif fn.endswith('.en'):
                print(textpath + f + '/' + fn, splitpath + f + '/')
                en_split_each_sentence(textpath + f + '/' + fn, splitpath + f + '/')

            index += 1


if __name__ == "__main__":
    textpath = 'D:/v2_extract/text/'
    splitpath = 'D:/v2_extract/split/'
    batch_split_files(textpath, splitpath)