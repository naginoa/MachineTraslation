import os
import string
import win32com
from win32com.client import Dispatch


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 计算句子中符号个数
def count_punc(st):
    flag = 0
    for s in st:
        if s in string.punctuation:
            flag += 1

    return flag


def closesoft():
    print('''挂载程序关闭中……''')
    import win32com.client
    wc = win32com.client.constants

    try:
        wps = win32com.client.gencache.EnsureDispatch('kwps.application')
    except:
        wps = win32com.client.gencache.EnsureDispatch('wps.application')
    else:
        wps = win32com.client.gencache.EnsureDispatch('word.application')
    try:
        wps.Documents.Close()
        wps.Documents.Close(wc.wdDoNotSaveChanges)
        wps.Quit
    except:
        pass


# 将PPT抽取文字,并返回应该删除的单个PPT
def ppt2txt(pairspath, textpath):
    dele_flist = []
    folder_dir_list = os.listdir(pairspath)
    for f in folder_dir_list:
        file_list = os.listdir(pairspath + f)
        flag = 0

        if not os.path.exists(textpath + f):
            os.mkdir(textpath + f)

        while flag <= len(file_list) - 1:
            if 'ppt' in file_list[flag].lower():
                pptname = pairspath + f + '/' + file_list[flag]
                textname = textpath + f + '/' + file_list[flag].rsplit('.', 1)[0]
                print(pptname, textname)

                try:
                    ppt = win32com.client.Dispatch('PowerPoint.Application')
                    ppt.Visible = 1

                    pptSel = ppt.Presentations.Open(pptname)
                    win32com.client.gencache.EnsureDispatch('PowerPoint.Application')

                    fi = open(textname, "w", encoding='utf-8')
                    slide_count = pptSel.Slides.Count
                    texts = []

                    for i in range(1, slide_count + 1):
                        shape_count = pptSel.Slides(i).Shapes.Count

                        for j in range(1, shape_count + 1):
                            if pptSel.Slides(i).Shapes(j).HasTextFrame:
                                s = pptSel.Slides(i).Shapes(j).TextFrame.TextRange.Text.strip().strip('.').strip('\t').strip('\n')
                                # 过滤空格 and 符号过多的句子 and 纯数字
                                if len(s) > 1 and count_punc(s) < 0.3 * len(s) and not is_number(s.strip().strip('.')) and s != '':
                                    texts.append(s)

                    # 去重并保持顺序
                    no_repe_texts = list(set(texts))
                    no_repe_texts.sort(key=texts.index)
                    for t in no_repe_texts:
                        print(t)
                        fi.write(t + '\n')

                    fi.close()
                    ppt.Quit()

                    # 去掉莫名其妙的空行
                    lines = []
                    with open(textname, encoding='utf-8') as fi:
                        lines = fi.readlines()

                    with open(textname, "w", encoding='utf-8') as fi:
                        for line in lines:
                            if line != '\n':
                                fi.write(line.strip().strip('\t') + '\n')

                except:
                    ppt.Quit()
                    print('cant extract!')

                    # ppt必须成对存在，如果有一者无法extract，则删除另一个
                    if flag % 2 == 0:
                        flag += 1
                        print(flag, textname)

                        dele_flist.append(textname)

                    else:
                        # os.remove(textpath + f + '/' + file_list[flag - 1].rsplit('.', 1)[0])
                        dele_flist.append(textpath + f + '/' + file_list[flag - 1].rsplit('.', 1)[0])

            flag += 1

    return dele_flist


def test_ppt():
    pptname = 'D:/v2_extract/pairs/200801/CDE meeting BIBF 1120_Topic 2b_final.en.ppt'
    textname = 'E:/CDE meeting BIBF 1120_Topic 2b_final.en'

    try:
        ppt = win32com.client.Dispatch('PowerPoint.Application')
        ppt.Visible = 1
        pptSel = ppt.Presentations.Open(pptname)
        win32com.client.gencache.EnsureDispatch('PowerPoint.Application')

        fi = open(textname, "w", encoding='utf-8')
        slide_count = pptSel.Slides.Count
        texts = []
        for i in range(1, slide_count + 1):
            shape_count = pptSel.Slides(i).Shapes.Count
            # print(shape_count)
            for j in range(1, shape_count + 1):
                if pptSel.Slides(i).Shapes(j).HasTextFrame:
                    s = pptSel.Slides(i).Shapes(j).TextFrame.TextRange.Text.strip().strip('.').strip('\t').strip('\n')
                    # 过滤空格 and 符号过多的句子 and 纯数字
                    if len(s) > 1 and count_punc(s) < 0.3 * len(s) and not is_number(s.strip().strip('.')) and s != '':
                        texts.append(s)

        # 去重并保持顺序
        no_repe_texts = list(set(texts))
        no_repe_texts.sort(key=texts.index)
        for t in no_repe_texts:
            print(t)
            fi.write(t + '\n')
        fi.close()
        ppt.Quit()
        # 去掉莫名其妙的空行
        lines = []
        with open(textname, encoding='utf-8') as fi:
            lines = fi.readlines()
        with open(textname, "w", encoding='utf-8') as fi:
            for line in lines:
                if line != '\n':
                    fi.write(line.strip().strip('\t') + '\n')

    except:
        ppt.Quit()
        print('cant extract!')


if __name__ == "__main__":
    pairspath = 'D:/v2_extract/pairs/'
    textpath = 'D:/v2_extract/text/'
    dele_flist = ppt2txt(pairspath, textpath)
    for df in dele_flist:
        os.remove(df)
    # test_ppt()
    # en_split_each_sentence('C:/Users/hao/PycharmProjects/extractPDF_v2/1.txt', 'E:/')