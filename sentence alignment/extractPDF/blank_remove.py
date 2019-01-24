filepath = ''
filename = '08-ormulationfP.txt'

with open(filepath + filename, encoding='utf-8') as f:
    for line in f.readlines():
        #remove blank line
        if line.count(' ') < len(line) - 1:
            #with open(filepath + filename + 'tep', 'a', encoding='utf-8') as ft:
            #    print(line.strip())
                #ft.write(line.strip() + '\n')
            print(line)
            for l in line:
                print(l)
