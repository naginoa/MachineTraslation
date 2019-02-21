from nltk.tokenize import sent_tokenize


filename = 'en.txt'
endchar = '.'


def en_split_each_sentence(senpath, splitpath):
    with open(senpath, encoding='utf-8') as f:
        # add .
        for line in f.readlines():
            newline = ''
            if line.strip().endswith(endchar):
                newline = line.strip()
            else:
                newline = line.strip() + endchar

            if newline.count(endchar) > 1:
                sublinelist = sent_tokenize(newline)
                # sublinelist = [i + endchar for i in newline.split(newchar)[:-1]]
                # print(sublinelist)
                with open(splitpath + senpath.split('/')[-1], 'a', encoding='utf-8') as f:
                    for i in sublinelist:
                        f.write(i + '\n')
            else:
                with open(splitpath + senpath.split('/')[-1], 'a', encoding='utf-8') as f:
                    f.write(newline + '\n')
                    
#en_split_each_sentence('D:/test/201810/5_Analytical Procedure@eng.txt', 'D:/')


'''with open(filename, encoding='utf-8') as f:
    #add .
    for line in f.readlines():
        newline = ''
        if line.strip().endswith(endchar):
            newline = line.strip()
        else:
            newline = line.strip() + endchar

        if newline.count(endchar) > 1:
            sublinelist = sent_tokenize(newline)
            #sublinelist = [i + endchar for i in newline.split(newchar)[:-1]]
            #print(sublinelist)
            with open('en_split.txt', 'a', encoding='utf-8') as f:
                for i in sublinelist:
                    f.write(i + '\n')
        else:
            with open('en_split.txt', 'a', encoding='utf-8') as f:
                f.write(newline + '\n')
'''