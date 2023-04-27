import PyPDF2

pdf = open("Ebook-WTICIFES2019.pdf","rb")

pdfReader = PyPDF2.PdfReader(pdf)
pages = pdfReader.pages

with open("complete.txt","w") as file:
    for page in pages:
        file.write(page.extract_text())
