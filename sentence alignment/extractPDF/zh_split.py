filename = 'zh.txt'
endchar = '。'


with open(filename, encoding='utf-8') as f:
    #add .
    for line in f.readlines():
        newline = ''
        if len(line) == 1:
            continue
        if line.strip().endswith(endchar):
            newline = line.strip()
        else:
            newline = line.strip() + endchar

        if newline.count(endchar) > 1:
            sublinelist = [i + endchar for i in newline.split(endchar)[:-1]]
            #print(sublinelist)
            with open('zh_split.txt', 'a', encoding='utf-8') as f:
                for i in sublinelist:
                    f.write(i + '\n')
        else:
            with open('zh_split.txt', 'a', encoding='utf-8') as f:
                f.write(newline + '\n')