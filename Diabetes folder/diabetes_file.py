"""
This file is for diabetes data pre-processing

"""
import PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_document = "Cover letter Deepmind.pdf"
pdf = PdfFileReader(pdf_document)

for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter
    current_page = pdf.getPage(page)
    pdf_writer.addPage(current_page)

    outputFilename = "example-page-{}.pdf".format(page + 1)
    with open(outputFilename, "wb") as out:
        pdf_writer.write(out)

        print("created", outputFilename)

#with open('diabetes_file.txt', 'w') as f:
#    f.write("\n\n".join(pdfFileobj))
