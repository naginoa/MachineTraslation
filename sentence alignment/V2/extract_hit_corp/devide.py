with open('cn.txt', encoding='utf-8') as f:
    flag = 0
    for i in f.readlines():
        if flag % 10 == 7 or flag % 10 == 8:
            with open('ch_valid.txt', 'a', encoding='utf-8') as g:
                g.write(i)
        elif flag % 10 == 9:
            with open('ch_test.txt', 'a', encoding='utf-8') as g:
                g.write(i)
        else:
            with open('ch_train.txt', 'a', encoding='utf-8') as g:
                g.write(i)
        flag += 1

with open('en.txt', encoding='utf-8') as f:
    flag = 0
    for i in f.readlines():
        if flag % 10 == 7 or flag % 10 == 8:
            with open('en_valid.txt', 'a', encoding='utf-8') as g:
                g.write(i)
        elif flag % 10 == 9:
            with open('en_test.txt', 'a', encoding='utf-8') as g:
                g.write(i)
        else:
            with open('en_train.txt', 'a', encoding='utf-8') as g:
                g.write(i)
        flag += 1

print('completed!')