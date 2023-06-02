import re
import pandas



query = r"\n([\W\w]*?)(\.\.)" 
pattern = re.compile(query)


text = ''


with open("../files.txt/sumario.txt", "r") as arquivo:
    text = arquivo.read()

list_items = []

for i in pattern.findall(text):
    list_items.append(i[0])



with open(r'../files.txt/sumario_formatado.txt', 'w') as fp:
    for item in list_items:
        # write each item on a new line
        fp.write("\n|%s|\n" % item)
    print('Done')


with open("../files.txt/sumario_formatado.txt", "r") as arquivo:
    text = arquivo.read()


###########################################################################

query2 = r"\n\|([\W\w]*?)(\n)" 
# query = r"Resumo([\S\s]*?)1. I"
pattern2 = re.compile(query2)
# remove_pattern = re.compile(r"1.([\w\W])*")

text2 = ''


with open("../files.txt/sumario_formatado.txt", "r") as arquivo:
    text2 = arquivo.read()

list_items2 = []

for i in pattern2.findall(text2):
    list_items2.append(i[0])



with open(r'../files.txt/Autores.txt', 'w') as fp:
    for item in list_items2:
        # write each item on a new line
        fp.write("\n|%s|\n" % item)
    print('Done')


####################################################################
    with open("../files.txt/Autores.txt", 'r') as file:
              filedata = file.read()  ##.replace('|', '')
             
print (filedata)  
text =' '
with open("../files.txt/Autores.txt", "r") as arquivo:
                  text = arquivo.read().replace('|', '')
                  

with open("../files.txt/Autores.txt", "w") as arquivo:
 arquivo.write(text)


print('Done')


with open("../files.txt/sumario_formatado.txt", "r") as arquivo:
    titulos = arquivo.read()

i = 0;

print(list_items2[i])
titulo=list_items2[0]
t=" "
while(i<len(list_items2)):
       print (i)
       titulo=list_items2[i]
       titulos= titulos.replace(titulo, "")
       i=i+1
   

titulos= titulos.replace("|", "")
with open("../files.txt/Titulos.txt", "w") as arquivo:
 arquivo.write(titulos)