##import PyPDF2
##
##pdfFile = open('p1.pdf','rb')
##pdfReader = PyPDF2.PdfFileReader(pdfFile)
##print(pdfReader.numPages)
##page = pdfReader.getPage(1)
##print(page.extractText().encode('gbk').decode('utf-8'))
##pdfFile.close()


#--------------------------2------------------------

import pdfplumber
file_path = r'豫A26QS6交强保单.pdf'

with pdfplumber.open(file_path) as pdf:
    page = pdf.pages[0]
    print(page.extract_text())
