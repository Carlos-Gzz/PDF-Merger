import PyPDF2, os
os.chdir('C:\\Users\\User\\Folder\\Folder n')
pdfFile1 = open('File1.pdf', 'rb')
pdfFile2 = open('File2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('CombinedFiles.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdfFile1.close()
pdfFile2.close()

