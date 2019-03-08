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

        index = 0

        while index <= len(file_list) - 2:
            for_fn = file_list[index]
            lat_fn = file_list[index + 1]
            # each_store_para(rootpath + f + '/' + file, storepath + f + '/')
            if for_fn.rsplit('.', 2)[0] == lat_fn.rsplit('.', 2)[0]:
                # print(for_fn, lat_fn)
                en_fn = for_fn if '.en' in for_fn.lower() else lat_fn
                zh_fn = for_fn if '.zh' in for_fn.lower() else lat_fn
                print(en_fn, zh_fn)
                index += 1

                tran_fn = en_fn.rsplit('.', 2)[0] + '.tran'
                if os.path.exists(transpath + f + '/' + tran_fn):
                    shutil.copyfile(splitpath + f + '/' + en_fn, segpath + f + '/' + en_fn)
                    each_segment(splitpath + f + '/' + zh_fn, segpath + f + '/' + zh_fn)
                    each_segment(transpath + f + '/' + tran_fn, segpath + f + '/' + tran_fn)

            index += 1


    '''
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
    '''


if __name__ == "__main__":
    splitpath = 'D:/v2_extract/split/'
    transpath = 'D:/v2_extract/translation/'
    segpath = 'D:/v2_extract/segmentation/'
    batch_segment(splitpath, transpath, segpath)