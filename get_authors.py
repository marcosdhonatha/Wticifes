import re
import pandas


## AINDA NÃO FUNCIONA!!!
query = r"\n([\W\w]*?)(\.\.)" ##\n([\W\w]*?)\.\.
# query = r"Resumo([\S\s]*?)1. I"
pattern = re.compile(query)
# remove_pattern = re.compile(r"1.([\w\W])*")

text = ''


with open("sumario.txt", "r") as arquivo:
    text = arquivo.read()

list_items = []

for i in pattern.findall(text):
    list_items.append(i[0])



with open(r'sumario_formatado.txt', 'w') as fp:
    for item in list_items:
        # write each item on a new line
        fp.write("\n|%s|\n" % item)
    print('Done')


with open("sumario_formatado.txt", "r") as arquivo:
    text = arquivo.read()


###########################################################################

query2 = r"\n\|([\W\w]*?)(\n)" 
# query = r"Resumo([\S\s]*?)1. I"
pattern2 = re.compile(query2)
# remove_pattern = re.compile(r"1.([\w\W])*")

text2 = ''


with open("sumario_formatado.txt", "r") as arquivo:
    text2 = arquivo.read()

list_items2 = []

for i in pattern2.findall(text2):
    list_items2.append(i[0])



with open(r'Autores.txt', 'w') as fp:
    for item in list_items2:
        # write each item on a new line
        fp.write("\n|%s|\n" % item)
    print('Done')


####################################################################
    with open("Autores.txt", 'r') as file:
              filedata = file.read()  ##.replace('|', '')
             
print (filedata)  
text =' '
with open("Autores.txt", "r") as arquivo:
                  text = arquivo.read().replace('|', '')
                  

with open("Autores.txt", "w") as arquivo:
 arquivo.write(text)
# # Replace the target string
# filedata = filedata.replace('|', '')

# # Write the file out again
# with open('Autores.txt', 'w') as file:
#   file.write(filedata)

# print (filedata)  

print('Done')