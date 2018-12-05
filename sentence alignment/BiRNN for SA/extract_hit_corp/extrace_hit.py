with open('data.txt', encoding='utf-8') as f:
    flag = 0
    for i in f.readlines():
        if flag % 2 == 0:
            with open('en.txt', 'a', encoding='utf-8') as g:
                g.write(i)
        else:
            with open('cn.txt', 'a', encoding='utf-8') as g:
                g.write(i)
        flag += 1

print('completed!')