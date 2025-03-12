import numpy as np
import re as REGEX
from enum import Enum

#tokens
#--------------------------------------------------------------------------------------------------
REid = '^[a-zA-Z]*(([a-zA-Z])|([0-9]))'
REtexto = "^\"+(.)"
RENumero ="^[0-9]+[0-9])"
#--------------------------------------------------------------------------------------------------

#Lee textod e un archivo y lo divide
#--------------------------------------------------------------------------------------------------
f = open("compilar.txt","r")

leido = f.read()

# dividido = f.split()#DEBO DE PONER PARENTESIS
modificado = leido.split()#como divide con espacios no puede detectar texto con espacios
#--------------------------------------------------------------------------------------------------


def comprobar( lexemaB, lexemaE):
    if(lexemaB == lexemaE):
        print("Es un -"+ lexemaB +"------->  " + lexemaE)
        return 1;

def ErrorSintactico(correcto, encontrado):
    print("Se encontro < " + encontrado +" >   el correcto era:  " + correcto)     
    
#multiples opciones
Imprimiples ={"TEXTO","DIGITO"}
OperadorLogico ={">","<","&&","!=","||",}
OperadorMatematico ={"+","-","*","/","^",}


#Tabla de simbolos
#--------------------------------------------------------------------------------------------------
class Tabladesimbolos:
    def __init__(self, pos ,tipo,lexema ):
        self.pos = pos
        self.tipo = tipo
        self.lexema = lexema
#--------------------------------------------------------------------------------------------------


tablita = []
for i in range(100):
    tablita.append(Tabladesimbolos(i,"",""))

tablita[0].pos =0
tablita[0].tipo ='int'
tablita[0].lexema ='int'

if(0):#-----------------------------------------------------------------------> Si lexiquea o no
    for i in range(len(modificado)):

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

