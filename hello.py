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
        #print(lexemaB +"-----------"+lexemaE)
        return 1;

def ErrorSintactico(correcto, encontrado):
    print("Se encontro < " + encontrado +" >   el correcto era:  " + correcto)     
    
def AnadirTablita(espacio, tipo, lexema):
    tablita[espacio].pos = espacio
    tablita[espacio].tipo = tipo
    tablita[espacio].lexema = lexema
    
    
#--------------------------------------------------------------------------------------------------
#multiples opciones
Imprimiples = {"TEXTO","DIGITO"}
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
for i in range(len(modificado)):
    tablita.append(Tabladesimbolos(i,"",""))


if(1):#-----------------------------------------------------------------------> Si lexiquea o no
    for i in range(len(modificado)):

        if comprobar("int",modificado[i]):
            AnadirTablita(i,'int',modificado[i])
            continue

        if comprobar("float",modificado[i]):
            AnadirTablita(i,'float',modificado[i])
            continue

        if comprobar(")",modificado[i]):
            AnadirTablita(i,')',modificado[i])
            continue

        if comprobar("(",modificado[i]):
            AnadirTablita(i,'(',modificado[i])
            continue

        if comprobar("{",modificado[i]):
            AnadirTablita(i,'{',modificado[i])
            continue

        if comprobar("}",modificado[i]):
            AnadirTablita(i,'}',modificado[i])
            continue

        if comprobar(";",modificado[i]):
            AnadirTablita(i,';',modificado[i])
            continue

        if comprobar("while",modificado[i]):
            AnadirTablita(i,'while',modificado[i])
            continue
        if comprobar("if",modificado[i]):
            AnadirTablita(i,'if',modificado[i])
            continue

        if comprobar("print",modificado[i]):
            AnadirTablita(i,'print',modificado[i])
            continue

        if comprobar("read",modificado[i]):
            AnadirTablita(i,'read',modificado[i])
            continue

        if comprobar("=",modificado[i]):
            AnadirTablita(i,'=',modificado[i])
            continue

        if comprobar("+",modificado[i]):
            AnadirTablita(i,'+',modificado[i])
            continue

        if comprobar("-",modificado[i]):
            AnadirTablita(i,'-',modificado[i])
            continue

        if comprobar("*",modificado[i]):
            AnadirTablita(i,'*',modificado[i])
            continue

        if comprobar("/",modificado[i]):
            AnadirTablita(i,'/',modificado[i])
            continue

        if comprobar("^",modificado[i]):
            AnadirTablita(i,'^',modificado[i])
            continue

        if comprobar(">",modificado[i]):
            AnadirTablita(i,'>',modificado[i])
            continue

        if comprobar("<",modificado[i]):
            AnadirTablita(i,'<',modificado[i])
            continue

        if comprobar("==",modificado[i]):
            AnadirTablita(i,'==',modificado[i])
            continue

        if comprobar("||",modificado[i]):
            AnadirTablita(i,'||',modificado[i])
            continue

        if comprobar("&&",modificado[i]):
            AnadirTablita(i,'&&',modificado[i])
            continue

        if comprobar("!=",modificado[i]):
            AnadirTablita(i,'!=',modificado[i])
            continue 

        #checar si es id
        Esid = REGEX.search(REid,modificado[i])
        if Esid:
            #print("Es un ID : "+modificado[i])
            AnadirTablita(i,'ID',modificado[i])
            continue

        #Checar si es texto
        Estexto = REGEX.search(REtexto, modificado[i])
        if Estexto:
           #print("Es un texto: "+ modificado[i])
            AnadirTablita(i,'TXT',modificado[i])
            continue

        #Checa si es numero
        Esnumero = modificado[i]
        if Esnumero.isdigit():
            #print("Es un numero: "+ modificado[i])
            AnadirTablita(i,'NUM',modificado[i])

#--------------------------------------------------------------------------------------------------
#Imprimir la tablita
if(0):
    for i in range(len(tablita)):
        print("----------")
        print(tablita[i].pos)
        print(tablita[i].tipo)
        print(tablita[i].lexema)

#--------------------------------------------------------------------------------------------------