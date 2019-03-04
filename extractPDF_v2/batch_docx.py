import os
from docx import Document
from extract_PPT import is_number, count_punc


def reback_add_zh(docxpath):
    folder_dir_list = os.listdir(docxpath)
    for f in folder_dir_list:
        file_list = os.listdir(docxpath + f)
        for file in file_list:
            if '.zh' not in file and '.en' not in file:
                os.rename(docxpath + f + '/' + file, docxpath + f + '/' + file.rsplit('.', 1)[0] + '.zh' + '.docx')


def each_store_para(pdfpath, storepath):
    pdfname = pdfpath.rsplit('/', 1)[-1]
    textname = pdfname.rsplit('.', 1)[0]
    document = Document(pdfpath)
    ps = document.paragraphs
    texts = []

    for p in ps:
        # 过滤空格 and 符号过多的句子 and 纯数字
        if len(p.text) > 1 and count_punc(p.text) < 0.3 * len(p.text) and not is_number(p.text.strip().strip('.')):
            texts.append(p.text.strip().strip('.'))

    # 去重并保持顺序
    no_repe_texts = list(set(texts))
    no_repe_texts.sort(key=texts.index)
    with open(storepath + textname, 'a', encoding='utf-8') as f:
        for t in no_repe_texts:
            print(t)
            f.write(t + '\n')


def batch_store_para(rootpath, storepath):
    folder_dir_list = os.listdir(rootpath)
    for f in folder_dir_list:
        file_list = os.listdir(rootpath + f)

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
                each_store_para(rootpath + f + '/' + en_fn, storepath + f + '/')
                each_store_para(rootpath + f + '/' + zh_fn, storepath + f + '/')
                index += 1

            index += 1


if __name__ == "__main__":
    docxpath = 'D:/v2_extract/docx/'
    textpath = 'D:/v2_extract/text/'
    # reback_add_zh(docxpath)
    batch_store_para(docxpath, textpath)