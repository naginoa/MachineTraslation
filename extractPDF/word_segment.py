import jieba


filename = './experdata/our_tran.txt'
with open(filename, encoding='utf-8') as f:
    for line in f.readlines():
        seg_list = jieba.cut(line, cut_all=False)
        writeline = ' '.join(seg_list)
        print(writeline)
        with open('our_tran_seg.txt', 'a', encoding='utf-8') as f2:
            f2.write(writeline)