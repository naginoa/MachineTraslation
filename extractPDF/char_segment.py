import os
import shutil


def rename_as_bleualign(splitpath, transpath):
    folder_dir_list = os.listdir(splitpath)
    for f in folder_dir_list:
        file_list = os.listdir(splitpath + f)
        i = 0
        while (i <= len(file_list) - 2):
            if '@eng' in file_list[i].lower():
                en = file_list[i]
                zh = file_list[i + 1]
                new_en = en[:-4].replace('@eng', '') + '.en'
                new_zh = new_en.replace('.en', '.zh')
            elif '@eng' in file_list[i + 1].lower():
                en = file_list[i + 1]
                zh = file_list[i]
                new_en = en[:-4].replace('@eng', '') + '.en'
                new_zh = new_en.replace('.en', '.zh')
            elif 'chi' in file_list[i].lower() or '译' in file_list[i].lower() or '中' in file_list[i].lower():
                en = file_list[i + 1]
                zh = file_list[i]
                new_en = en[:-4] + '.en'
                new_zh = new_en.replace('.en', '.zh')
            elif 'chi' in file_list[i + 1].lower() or '译' in file_list[i + 1].lower() or '中' in file_list[
                i + 1].lower():
                en = file_list[i]
                zh = file_list[i + 1]
                new_en = en[:-4] + '.en'
                new_zh = new_en.replace('.en', '.zh')

            i += 2

            print(splitpath + f + '/' + en, splitpath + f + '/' + new_en)
            os.rename(splitpath + f + '/' + en, splitpath + f + '/' + new_en)
            os.rename(splitpath + f + '/' + zh, splitpath + f + '/' + new_zh)


    folder_dir_list2 = os.listdir(transpath)
    for f2 in folder_dir_list2:
        file_list2 = os.listdir(transpath + f2)
        for file2 in file_list2:
            new_tran = file2[:-4].replace('@eng', '').replace('@tran', '') + '.tran'
            print(transpath + f2 + '/' + file2, transpath + f2 + '/' + new_tran)
            os.rename(transpath + f2 + '/' + file2, transpath + f2 + '/' + new_tran)


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




splitpath = 'D:/split2/'
transpath = 'D:/translation/'
segpath = 'D:/segment/'
#rename_as_bleualign(splitpath, transpath)
batch_segment(splitpath, transpath, segpath)


'''
filename = './experdata/our_tran.txt'
with open(filename, encoding='utf-8') as f:
    for line in f.readlines():
        writeline = ' '.join(line)
        print(writeline)
        with open('our_tran_seg_char.txt', 'a', encoding='utf-8') as f2:
            f2.write(writeline)
'''