import os


resultpath = 'D:/final_result/'
mergepath = 'E:/result/'


folder_dir_list = os.listdir(resultpath)
for f in folder_dir_list:
    file_list = os.listdir(resultpath + f)
    for file in file_list:
        if file.endswith('zh.aligned'):
            with open(resultpath + f + '/' + file, encoding='utf-8') as f1:
                for line in f1.readlines():
                    with open(mergepath + 'zh.txt', 'a', encoding='utf-8') as f2:
                        f2.write(line)
        elif file.endswith('en.aligned'):
            with open(resultpath + f + '/' + file, encoding='utf-8') as f1:
                for line in f1.readlines():
                    with open(mergepath + 'en.txt', 'a', encoding='utf-8') as f2:
                        f2.write(line)