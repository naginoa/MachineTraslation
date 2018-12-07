with open('test.ref', 'w', encoding='utf-8') as f:
    flag = 1
    for i in range(1, 20):
        f.write(str(i) + '\t' + str(i) + '\n')
