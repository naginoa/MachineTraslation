filename = './experdata/our_tran.txt'
with open(filename, encoding='utf-8') as f:
    for line in f.readlines():
        writeline = ' '.join(line)
        print(writeline)
        with open('our_tran_seg_char.txt', 'a', encoding='utf-8') as f2:
            f2.write(writeline)