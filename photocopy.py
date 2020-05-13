import os
import sys
import shutil

def removeSpace(string): 
    newstring = string.replace(" ", "") 
    return newstring.replace("\n", "") 

def copyPhotos(pics,prefix):
    path = os.getcwd()
    print(path)
    if not os.path.isdir(path+"/tmp"):
        print("Creating folder: "+path+"/tmp")
        os.makedirs(path+"/tmp")            
    for pic in pics:
        file = prefix + pic + ".jpg"
        print("Copiando arquivo "+path+"/"+file)
        if os.path.exists(path+"/"+file):
            shutil.copyfile(path+ "/"+file, path+"/tmp/"+file)
        else :
            print("Arquivo "+file+ " não encontrado.")

print("Arquivo txt das fotos: ")
filename = input()
print("Digite o prefixo do arquivo de foto:")
prefix = input()
print("*************************************************")
lines = ""
for line in open(filename, 'r'):
    lines += removeSpace(line)
linesArr = lines.split(',')
copyPhotos(linesArr,prefix)