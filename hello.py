import numpy as np
import re as REGEX
from enum import Enum
import sys

#tokens
#--------------------------------------------------------------------------------------------------
REid = '^[a-zA-Z_][a-zA-Z0-9_]*$'
REtexto = "^\"+(.)"
RENumero ="^[0-9]+[0-9])"

OperadorLogico =[">","<","&&","!=","||",'==']
OperadorMatematico =["+","-","*","/","^"]


pasos = 0
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
    sys.exit()     
    
def AnadirTablita(espacio, tipo, lexema):
    tablita[espacio].pos = espacio
    tablita[espacio].tipo = tipo
    tablita[espacio].lexema = lexema
    
    
#--------------------------------------------------------------------------------------------------
#multiples opciones
Imprimiples = ["TXT","ID"]

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
        
        if comprobar("string",modificado[i]):
            AnadirTablita(i,'string',modificado[i])
            continue
        
        if comprobar("while",modificado[i]):
            AnadirTablita(i,'while',modificado[i])
            continue
        
        #Checa si es operador matematico    
        for i2 in range(len(OperadorMatematico)):
            if(OperadorMatematico[i2] == modificado[i]):
                AnadirTablita(i,"OpM",modificado[i])
                break
        if(OperadorMatematico[i2] == modificado[i]): continue
                
        #checa si es operador logico
        for i2 in range(len(OperadorLogico)):
            if(OperadorLogico[i2] == modificado[i]):
                AnadirTablita(i,"OpL",modificado[i])
                break
        if(OperadorLogico[i2] == modificado[i]): 
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
            continue
            
         #checar si es id
        Esid = REGEX.search(REid,modificado[i])
        if Esid:
            #print("Es un ID : "+modificado[i])
            AnadirTablita(i,'ID',modificado[i])
            continue
        
        try:
            num =float(modificado[i])
            AnadirTablita(i,'decimal',modificado[i])
        except ValueError:
            ErrorSintactico("PALALBRA VALIDA", modificado[i])
        
#--------------------------------------------------------------------------------------------------
#Imprimir la tablita
if(0):
    for i in range(len(tablita)):
        print("----------")
        print(tablita[i].pos)
        print(tablita[i].tipo)
        print(tablita[i].lexema)

#--------------------------------------------------------------------------------------------------
#no Terminales
OpM ="OpM"
inicial = ["int","float","string","print","read"]
OpL= 'OpL'
final = ';'
INT =["ID","="] 
INTC = ["OpM","NUM"]
valoresNumericos = ['NUM','ID']
valoresdecimales = ['decimal','ID']
valoresComparables = ['NUM','ID','decimal']
patronWhile =['(','ID',OpL,'ID',')','{',]
patronString =['ID','=','TXT',';']
patronImprimirDer = ['(']
patronImprimirIzq = [')',';']  
patronLectura = ['(',')',';']
patronPreguntaIzq = [')','{']


#--------------------------------------------------------------------------------------------------        

def Sintactico(numero):#RECURSIVO
    global pasos
    if(pasos < len((tablita))-1):
        match numero:
            case 1:   
                match tablita[pasos].lexema:
                    case "int":
                        pasos += 1
                        Sintactico(2)
                    case "float":
                        pasos += 1
                        Sintactico(3)
                    case "string":
                        pasos += 1
                        Sintactico(4)
                    case "print":
                        pasos += 1
                        Sintactico(5)
                    case "read":
                        pasos += 1
                        Sintactico(6)
                    case "while":
                        pasos += 1
                        Sintactico(7)
                    case "if":
                        pasos += 1
                        Sintactico(8) 
                
            case 2:#int
                    for i in range(len(INT)):#Es int?
                        if(tablita[pasos].tipo == INT[i]):
                            pasos += 1
                            continue
                        else:
                            ErrorSintactico(INT[i],tablita[pasos].lexema)
                            
                    for i in range(len(valoresNumericos)):#Es valor numerico valido?

                        if(tablita[pasos].tipo == valoresNumericos[i]):
                            pasos += 1
                            break
                        if(i< len(valoresNumericos)): continue
                        
                        ErrorSintactico("Valor numerico (Numero o ID)",tablita[pasos].lexema)
                    
                    if(tablita[pasos].tipo == OpM):
                        pasos += 1
                        for i in range(len(valoresNumericos)):#Es valor numerico valido?

                            if(tablita[pasos].tipo == valoresNumericos[i]):
                                pasos += 1
                                break
                            if(i< len(valoresNumericos)): continue
                            
                            ErrorSintactico("Valor numerico (Numero o ID)",tablita[pasos].lexema)
                        
                        if(tablita[pasos].tipo == OpM):
                            pasos += 1
                            for i in range(len(valoresNumericos)):#Es valor numerico valido?

                                if(tablita[pasos].tipo == valoresNumericos[i]):
                                    pasos += 1
                                    break
                                if(i< len(valoresNumericos)): continue
                                
                                ErrorSintactico("Valor numerico (Numero o ID)",tablita[pasos].lexema)
                            if(tablita[pasos].tipo == ";"):
                                pasos += 1
                                Sintactico(1)
                            else:
                                ErrorSintactico(";",tablita[pasos].lexema)
                        elif(tablita[pasos].tipo == ";"):
                            pasos += 1
                            Sintactico(1)
                        else:
                            ErrorSintactico(";",tablita[pasos].lexema)                                                                           
                    elif(tablita[pasos].tipo == ";"):
                        pasos += 1
                        Sintactico(1)
                    else:
                        ErrorSintactico(";",tablita[pasos].lexema)
            
            case 3:#float
                    for i in range(len(INT)):#Es float?
                        if(tablita[pasos].tipo == INT[i]):
                            pasos += 1
                            continue
                        else:
                            ErrorSintactico(INT[i],tablita[pasos].lexema)
                            
                    for i in range(len(valoresdecimales)):#Es valor numerico valido?

                        if(tablita[pasos].tipo == valoresdecimales[i]):
                            pasos += 1
                            break
                        if(i< len(valoresdecimales)): continue
                        
                        ErrorSintactico("Valor numerico (Numero o ID)",tablita[pasos].lexema)
                    
                    if(tablita[pasos].tipo == OpM):
                        pasos += 1
                        for i in range(len(valoresdecimales)):#Es valor numerico valido?

                            if(tablita[pasos].tipo == valoresdecimales[i]):
                                pasos += 1
                                break
                            if(i< len(valoresdecimales)): continue
                            
                            ErrorSintactico("Valor numerico (Numero o ID)",tablita[pasos].lexema)
                        
                        if(tablita[pasos].tipo == OpM):
                            pasos += 1
                            for i in range(len(valoresdecimales)):#Es valor numerico valido?

                                if(tablita[pasos].tipo == valoresdecimales[i]):
                                    pasos += 1
                                    break
                                if(i< len(valoresdecimales)): continue
                                
                                ErrorSintactico("Valor numerico (Numero o ID)",tablita[pasos].lexema)
                            if(tablita[pasos].tipo == ";"):
                                
                                Sintactico(1,pasos+1)
                            else:
                                ErrorSintactico(";",tablita[pasos].lexema)
                        elif(tablita[pasos].tipo == ";"):
                            pasos += 1
                            Sintactico(1)
                        else:
                            ErrorSintactico(";",tablita[pasos].lexema)                                                                           
                    elif(tablita[pasos].tipo == ";"):
                        pasos += 1
                        Sintactico(1)
                    else:
                        ErrorSintactico(";",tablita[pasos].lexema)         

            case 7:#while
                for i in range(len(patronWhile)):#Es float?
                        if(tablita[pasos].tipo == patronWhile[i]):
                            pasos += 1
                            continue
                        else:
                            ErrorSintactico(INT[i],tablita[pasos].lexema)
                
                Sintactico(1)
                
                if(tablita[pasos].tipo == '}'):
                    pasos += 1
                    Sintactico(1)
                else:
                    ErrorSintactico("}",tablita[pasos].lexema)
                
            case 4:#string
                for i in range(len(patronString)):#Es float?
                        if(tablita[pasos].tipo == patronString[i]):
                            pasos += 1
                            continue
                        else:
                            ErrorSintactico(INT[i],tablita[pasos].lexema)
                Sintactico(1)

            case 5:#print
                if (tablita[pasos].tipo == patronImprimirDer[0]):
                    pasos += 1
                else:
                    ErrorSintactico("(",tablita[pasos].lexema)
                
                for i in range(len(Imprimiples)):
                    if(tablita[pasos].tipo == Imprimiples[i]):
                        pasos += 1
                        break
                    
                    if(i< len(Imprimiples)): continue
                    ErrorSintactico(Imprimiples[i],tablita[pasos].lexema)
                
                for i in range(len(patronImprimirIzq)):
                    if(tablita[pasos].tipo == patronImprimirIzq[i]):
                        pasos += 1
                        continue
                    else:
                        ErrorSintactico(patronImprimirIzq[i],tablita[pasos].lexema)
                                    
                Sintactico(1)
                
            case 6:#read
                for i in range(len(patronLectura)):
                    if(tablita[pasos].tipo == patronLectura[i]):
                        pasos += 1
                        continue
                    else:
                        ErrorSintactico(patronLectura[i],tablita[pasos].lexema)

            case 8:#Pregunta
                if(tablita[pasos].tipo == '('):
                    pasos += 1
                else:
                    ErrorSintactico('(',tablita[pasos].lexema)
                
                for i in range(len(valoresComparables)):
                    if(tablita[pasos].tipo == valoresComparables[i]):
                        pasos += 1
                        break
                    
                    if(i< len(valoresComparables)): continue
                    ErrorSintactico(valoresComparables[i],tablita[pasos].lexema)
                    
                if(tablita[pasos].tipo == OpL):
                    pasos += 1
                else:
                    ErrorSintactico(OpL,tablita[pasos].lexema)
            
                for i in range(len(valoresComparables)):
                        if(tablita[pasos].tipo == valoresComparables[i]):
                            pasos += 1
                            break
                        
                        if(i< len(valoresComparables)): continue
                        ErrorSintactico(valoresComparables[i],tablita[pasos].lexema)
            
                for i in range(len(patronPreguntaIzq)):
                    if(tablita[pasos].tipo == patronPreguntaIzq[i]):
                        pasos += 1
                        continue
                    else:
                        ErrorSintactico(patronPreguntaIzq[i],tablita[pasos].lexema)
                
                Sintactico(1)        
                
                if(tablita[pasos].tipo == '}'):     
                    pasos += 1
                    Sintactico(1)
                else:
                    ErrorSintactico("}",tablita[pasos].lexema)
                
            
#--------------------------------------------------------------------------------------------------
                  
Sintactico(1)          
                    
#-------------------------------------------------------------------------------------------------- 
#Semantico                
                   

                        
                
                
        