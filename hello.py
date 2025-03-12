import numpy as np
import re as REGEX
from enum import Enum

#tokens
REid = '^[a-zA-Z]*(([a-zA-Z])|([0-9]))'
REtexto = "^(\")+(([a-zA-Z])|([0-9]))"
RENumero ="^[0-9]+[0-9])"



#leer texto
f = open("compilar.txt","r")

leido = f.read()

# dividido = f.split()#DEBO DE PONER PARENTESIS
modificado = leido.split()

def comprobar( lexemaB, lexemaE):
    if(lexemaB == lexemaE):
        print("Es un -"+ lexemaB +"------->  " + lexemaE)
        return 1;
        


for i in range(len(modificado)):
    #print(modificado[i])
    
    if comprobar("int",modificado[i]):
        
        continue
    
    if comprobar("float",modificado[i]):
        
        continue
    
    if comprobar(")",modificado[i]):
        
        continue
    
    if comprobar("(",modificado[i]):
        
        continue
    
    if comprobar("{",modificado[i]):
        
        continue
    
    if comprobar("}",modificado[i]):
        
        continue
    
    if comprobar(";",modificado[i]):
        
        continue
    
    if comprobar("while",modificado[i]):
        
        continue
    if comprobar("if",modificado[i]):
        
        continue
    
    if comprobar("print",modificado[i]):
        
        continue
    
    if comprobar("read",modificado[i]):
        
        continue
    
    if comprobar("=",modificado[i]):
        
        continue
    
    if comprobar("+",modificado[i]):
        
        continue
    
    if comprobar("-",modificado[i]):
        
        continue
    
    if comprobar("*",modificado[i]):
        
        continue
    
    if comprobar("/",modificado[i]):
        
        continue
    
    if comprobar("^",modificado[i]):
        
        continue
    
    if comprobar(">",modificado[i]):
        
        continue
    
    if comprobar("<",modificado[i]):
        
        continue
    
    if comprobar("==",modificado[i]):
        
        continue
    
    if comprobar("||",modificado[i]):
        
        continue
    
    if comprobar("&&",modificado[i]):
        
        continue
    
    if comprobar("!=",modificado[i]):
        
        continue 

    #checar si es id
    Esid = REGEX.search(REid,modificado[i])
    if Esid:
        print("Es un ID : "+modificado[i])
        continue
    
    #Checar si es texto
    Estexto = REGEX.search(REtexto, modificado[i])
    if Estexto:
        print("Es un texto: "+ modificado[i])
        continue
    
    #Checa si es numero
    Esnumero = modificado[i]
    if Esnumero.isdigit():
        print("Es un numero: "+ modificado[i])

