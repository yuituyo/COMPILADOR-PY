import numpy as np


#leer texto
f = open("compilar.txt","r")

leido = f.read()

# dividido = f.split()#DEBO DE PONER PARENTESIS
modificado = leido.split()


for x in modificado:
    print(modificado.pop())




