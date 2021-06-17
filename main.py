from PyPDF2 import PdfFileMerger

pdfs = ['pdf-file']


marger = PdfFileMerger()

for pdf in pdfs:
    marger.append(pdf)

marger.write("result/example.pdf")
marger.close()
