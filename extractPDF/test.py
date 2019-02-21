import os
import pickle
import string
import random


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def count_punc(st):
    flag = 0
    for s in st:
        if s in string.punctuation:
            flag += 1

    return flag


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""

    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':

        return True

    else:

        return False


root_dir = 'D:/experdata/'
folder_dir_list = os.listdir(root_dir)
for f in folder_dir_list:
    #print(f, len(os.listdir(root_dir + f)))
    file_list = os.listdir(root_dir + f)
    print(f, len(file_list))

    not_ppt_list = [i for i in file_list if '.ppt' not in str(i)]
    print(f, len(not_ppt_list))

    ppt_list = [i for i in file_list if '.ppt' in str(i)]
    print(ppt_list)



f2 = open('D:/pickle/dump.txt', 'rb')
d = pickle.load(f2)
f2.close()
print(d)

print(string.punctuation)
print(count_punc('The weight of each strip (10 vials) should be 12.5 ± 2 g.'))
print(len('The weight of each strip (10 vials) should be 12.5 ± 2 g.'))
print(count_punc('The weight of each strip (10 vials) should be 12.5 ± 2 g.') < 0.3*len('The weight of each strip (10 vials) should be 12.5 ± 2 g.'))
print(count_punc('___________    ______'))
print(len('___________    ______'))
print(count_punc('___________    ______') < 0.3 * len('___________    ______'))

print(is_number('dasdsa'))

for i in os.listdir('D:/test/200907-09'):
    print(i)


sss = '''
ABCD.
DESCRIPTION OF THE DRUG PRODUCT.
BEA 2180 BR Respimat solution for inhalation consists of an aqueous solution of.
BEA 2180 BR filled into a cartridge, and a Respimat inhalation device.
One cartridge is used per device.
Respimat is a hand held, pocket sized oral inhalation device that uses mechanical energy to generate a slow moving aerosol cloud of medication (“soft mist”) from a metered volume of drug solution.
Three dose strengths of BEA 2180 BR Respimat solution for inhalation, corresponding to 50, 100 and 200 µg and a placebo formulation will be used.
One dose will be administered by 2 actuations of the inhalation device.
In order to conform to international standards for declaration of active substances, the dose strengths refer to the cation, i.e.
BEA 2180, as the active moiety of the molecule.
COMPOSITION OF THE DRUG PRODUCT.
BEA 2180 BR RESPIMAT SOLUTION FOR INHALATION.
The BEA 2180 BR Respimat formulation is an aqueous solution containing BEA 2180 BR as active substance.
The compositions of BEA 2180 BR Respimat solution for inhalation corresponding to the dose strengths of 50, 100, and 200 µg as well as the placebo formulation are given in Table 1 and 2.
Table 1	Composition of BEA 2180 BR Respimat solution for inhalation (Mass per dose).
1 g of BEA 2180 corresponds to 1.211 g of BEA 2180 BR.
The declared amount of benzalkonium chloride refers to the anhydrous substance.
Benzalkonium chloride may be used as a 50% aqueous solution or solid substance; both comply with the respective monographs of the Pharm.
Eur.
"Benzalkonium chloride solution" and "Benzalkonium chloride", respectively.
One dose will be administered by 2 actuations of the inhalation device.
The placebo formulation used for clinical trials is identical to the active product formulation, except that it contains no active drug.
f	Alternatively, Purified Water may be used.
Table 2	Composition of BEA 2180 BR Respimat solution for inhalation (Percentage formula).
'''

def getText(string):
    list = []
    randline = random.random() * 500
    while len(string) > 1500:
        index = string.find("\n", int(randline) + 1000)
        if index is not None:
            list.append(string[0:index])
            string = string[index:]
    list.append(string)
    return list

for i in getText(sss):
    print(i)
    print(len(sss))
    print('----')
#print(getText(sss))
