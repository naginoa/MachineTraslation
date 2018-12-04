with open('test.ref', 'a', encoding='utf-8') as f:
    flag = 1
    for i in range(1, 1000):
        f.write(str(i) + '\t' + str(i) + '\n')
