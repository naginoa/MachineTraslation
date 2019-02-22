import os


def remove_space(bleupath, resultpath):
    folder_dir_list = os.listdir(bleupath)
    for f in folder_dir_list:
        file_list = os.listdir(bleupath + f)
        if not os.path.exists(resultpath + f):
            os.mkdir(resultpath + f)
        for file in file_list:
            if file.endswith('zh.aligned'):
                with open(bleupath + f + '/' + file, encoding='utf-8') as f1:
                    for line in f1.readlines():
                        writeline = ' '.join(filter(lambda x: x, line.split(' ')))
                        writeline = writeline.replace(' ', '').replace('\t', ' ').replace('', '').replace('', '')
                        writeline = ' '.join(filter(lambda x: x, writeline.split(' ')))
                        print(writeline)
                        with open(resultpath + f + '/' + file, 'a', encoding='utf-8') as f2:
                            f2.write(writeline)


            elif file.endswith('en.aligned'):
                with open(bleupath + f + '/' + file, encoding='utf-8') as f1:
                    for line in f1.readlines():
                        writeline = line.replace('  ', '').replace('\t', ' ').replace('', '')
                        print(writeline)
                        with open(resultpath + f + '/' + file, 'a', encoding='utf-8') as f2:
                            f2.write(writeline)


bleupath = 'D:/result_bleu/'
resultpath = 'D:/final_result/'
remove_space(bleupath, resultpath)