from docx import Document


pdfname = 'D:/cooked_data/200901-03/PK数据Rpt_LVFP王.docx'
document = Document(pdfname)
ps = document.paragraphs

#print(len(ps))
for p in ps:
    if len(p.text) > 1:
        #with open('zh.txt', 'a', encoding='utf-8') as f:
        #    f.write(p.text + '\n')
        #    print(p.text)
        print(p.text)