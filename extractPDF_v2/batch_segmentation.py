import os
import shutil


def each_segment(oripath, segpath):
    with open(oripath, encoding='utf-8') as f:
        for line in f.readlines():
            writeline = ' '.join(line)
            print(writeline)
            with open(segpath, 'a', encoding='utf-8') as f2:
                f2.write(writeline)


def batch_segment(splitpath, transpath, segpath):
    folder_dir_list = os.listdir(splitpath)
    for f in folder_dir_list:
        file_list = os.listdir(splitpath + f)
        if not os.path.exists(segpath + f):
            os.mkdir(segpath + f)
        for file in file_list:
            if file.endswith('.zh'):
                each_segment(splitpath + f + '/' + file, segpath + f + '/' + file)
            elif file.endswith('.en'):
                shutil.copyfile(splitpath + f + '/' + file, segpath + f + '/' + file)

    folder_dir_list2 = os.listdir(transpath)
    for f2 in folder_dir_list2:
        file_list2 = os.listdir(transpath + f2)
        for file2 in file_list2:
            each_segment(transpath + f2 + '/' + file2, segpath + f2 + '/' + file2)


if __name__ == "__main__":
    splitpath = 'D:/split/'
    transpath = 'D:/translation/'
    segpath = 'D:/segmentation/'
    batch_segment(splitpath, transpath, segpath)