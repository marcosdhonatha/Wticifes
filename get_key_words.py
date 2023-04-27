import re
import pandas
import PyPDF2

pdf = open("Ebook-WTICIFES2019.pdf","rb")

pdfReader = PyPDF2.PdfReader(pdf)
pages = pdfReader.pages

with open("complete.txt","w") as file:
    for page in pages:
        file.write(page.extract_text())


query = r"Palavras-chave([\w\W]*?)(1. I)"
# query = r"Resumo([\S\s]*?)1. I"
pattern = re.compile(query)
# remove_pattern = re.compile(r"1.([\w\W])*")

text = ''


with open("complete.txt", "r") as arquivo:
    text = arquivo.read()

list_items = []

for i in pattern.findall(text):
    list_items.append(i[0])

pandas.Series(list_items).to_csv("Palavraschaves.csv")