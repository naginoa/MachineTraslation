flags = [0, 0, 0, 0, 0, 0]


with open('y_scores', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        score = line.split('\t')[0]
        label = line.split('\t')[1]
        if float(label) :
            print(score)
            if float(score) <= 0.01:
                flags[0] += 1
            elif float(score) > 0.01 and float(score) <= 0.1:
                flags[1] += 1
            elif float(score) > 0.1 and float(score) <= 0.3:
                flags[2] += 1
            elif float(score) > 0.3 and float(score) <= 0.5:
                flags[3] += 1
            elif float(score) > 0.5 and float(score) <= 0.7:
                flags[4] += 1
            else:
                flags[5] += 1

print('the numbers of score_count <= 0.01 is {}'.format(flags[0]))
print('the numbers of score_count > 0.01 and <= 0.1 is {}'.format(flags[1]))
print('the numbers of score_count > 0.1 and <= 0.3 is {}'.format(flags[2]))
print('the numbers of score_count > 0.3 and <= 0.5 is {}'.format(flags[3]))
print('the numbers of score_count > 0.5 and <= 0.7 is {}'.format(flags[4]))
print('the numbers of score_count > 0.7 is {}'.format(flags[5]))
