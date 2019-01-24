from docx import Document


pdfpath = 'D:/cooked_data/200901-03/PK数据Rpt_LVFP王.docx'
storepath = 'D:/server/'
def store_para(pdfpath, storepath):
    pdfname = pdfpath.split('/')[-1][:-5]
    document = Document(pdfpath)
    ps = document.paragraphs

    for p in ps:
        if len(p.text) > 1:
            with open(storepath + pdfname + '.txt', 'a', encoding='utf-8') as f:
                f.write(p.text.strip() + '\n')
                print(p.text)
            #print(p.text)


store_para('D:/cooked_data/200803/S5A.docx', storepath)