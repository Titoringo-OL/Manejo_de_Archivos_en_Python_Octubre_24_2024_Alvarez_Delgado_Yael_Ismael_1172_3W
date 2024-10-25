# 2

# Para abrir el archivo, utilice la función incorporada open().
# La open()función devuelve un objeto de archivo, que tiene un read()método para leer el contenido del archivo:
# Ejemplo 

print("Alvarez Delgado Yael Ismael 1172 3W")
print(" ")
f = open("DemoFile.txt", "r")
print(f.read())

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

f = open("DemoFile.txt", "r")
print(f.read())

f = open("demofile2.txt", "a")
f.write("Ahora el archivo tiene mas contenido!")
f.close()

# Abrir y leer el archivo despues de agregar contenido:
f = open("demofile2.txt", "r")
print(f.read())

#Abra el archivo "demofile3.txt" y sobrescriba el contenido:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
.close()

#Abrir y leer el archivo despues de sobrescribirlo:
f = open("demofile3.txt", "r")
print(f.read())

import os
os.remove("demofile3.txt")

import os
if os.path.exists("demofile1.txt"):
  os.remove("demofile1.txt")
else:
  print("Este archivo no existe")


import os
os.rmdir("CarpetaDePrueba")
