from PyPDF2 import PdfFileWriter, PdfFileReader

outputfile = PdfFileWriter()

pdffile = PdfFileReader("teste.pdf")

numOfPages = pdffile.numPages

for i in range(numOfPages):
    page = pdffile.getPage(i)

    outputfile.addPage(page)

password = "senha"

outputfile.encrypt(password)

with open("teste_criptografado.pdf", "wb") as f:
    outputfile.write(f)