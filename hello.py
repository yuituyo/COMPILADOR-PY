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
    def __init__(self, pos ,tipo,lexema, expresiones,arbol):
        self.pos = pos
        self.tipo = tipo
        self.lexema = lexema
        self.expresiones = expresiones
        self.arbol = arbol
        
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
#--------------------------------------------------------------------------------------------------


tablita = []
for i in range(len(modificado)):
    tablita.append(Tabladesimbolos(i,"","",None,None))


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
def prRed(skk): print("\033[91m {}\033[00m" .format(skk) , end= '')
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk) )
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

#Imprimir la tablita
def Imprimirtabla():
    for i in range(len(tablita)):
        print('')
        print("----------")
        if(tablita[i].expresiones == None and tablita[i].tipo != 'ID' ):
            
            print('Posiscion:  ' , tablita[i].pos ,  'Tipo: ' ,  tablita[i].tipo, 'Lexema: ', tablita[i].lexema)
            
        elif(tablita[i].expresiones ==  None and tablita[i].tipo == 'ID' ):
            
            print('Posiscion:  ' , tablita[i].pos ,  'Tipo: ' ,  tablita[i].tipo, 'Lexema: ', end= ' ')
            prYellow(tablita[i].lexema) 
            
        else:
            print('Posiscion:  ' , tablita[i].pos ,  'Tipo: ' ,  tablita[i].tipo, end= ' ')
            prGreen(tablita[i].lexema)
            prRed( 'Expresiones: ' )
            prRed(tablita[i].expresiones)
 
#--------------------------------------------------------------------------------------------------
#no Terminales
OpM ="OpM"
inicial = ["int","float","string","print","read"]
OpL= 'OpL'
final = ';'
INT =["ID","="] 
INTC = ["OpM","NUM"]
valoresNumericos = ['NUM','ID']
valoresdecimales = ['decimal','ID','NUM']
valoresComparables = ['NUM','ID','decimal']
patronWhile =['(','ID',OpL,'ID',')','{',]
patronString =['ID','=','TXT',';']
patronImprimirDer = ['(']
patronImprimirIzq = [')',';']  
patronLectura = ['(', 'ID' , ')',';']
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
   
def AgregarExpresionesatabla():
    valor = 0
    for i in range(len(tablita)):
        if(tablita[i].lexema == '=' and tablita[i-1].tipo == 'ID'):
            valor = i+1
            lista =[]
            while(tablita[valor].lexema != ';'):
                lista.append(tablita[valor].lexema)
                valor += 1
            tablita[i-1].expresiones = lista
            continue
        
# Función para determinar la precedencia de los operadores
def infijo_a_prefijo(expresion_infija):
    """
    Convierte una expresión matemática en notación infija a notación prefija
    
    Args:
        expresion_infija: String con la expresión en notación infija (ej. "(3 + 4) * 5")
        
    Returns:
        String con la expresión en notación prefija (ej. "* + 3 4 5")
    """
    # Paso 1: Invertir la expresión infija
    expresion_invertida = invertir_expresion(expresion_infija)
    
    # Paso 2: Convertir a postfijo (pero de la expresión invertida)
    expresion_postfija = infijo_a_postfijo(expresion_invertida)
    
    # Paso 3: Invertir el postfijo para obtener prefijo
    expresion_prefija = expresion_postfija[::-1]
    
    return expresion_prefija

def invertir_expresion(expresion):
    """
    Invierte la expresión intercambiando paréntesis y el orden de los caracteres
    
    Args:
        expresion: String con la expresión original
        
    Returns:
        String con la expresión invertida
    """
    expresion = expresion.replace(' ', '')  # Eliminar espacios
    # Invertir la cadena y cambiar paréntesis
    invertida = []
    for char in expresion[::-1]:
        if char == '(':
            invertida.append(')')
        elif char == ')':
            invertida.append('(')
        else:
            invertida.append(char)
    return ''.join(invertida)

def precedencia(operador):
    """
    Devuelve la precedencia de un operador
    
    Args:
        operador: String con el operador (+, -, *, /, ^)
        
    Returns:
        Valor numérico de precedencia (mayor número = mayor precedencia)
    """
    if operador == '^':
        return 4
    elif operador in ['*', '/']:
        return 3
    elif operador in ['+', '-']:
        return 2
    else:
        return 0

def infijo_a_postfijo(expresion):
    """
    Convierte una expresión infija a postfija usando el algoritmo shunting-yard
    
    Args:
        expresion: String con la expresión infija
        
    Returns:
        String con la expresión postfija
    """
    pila = []
    salida = []
    
    for caracter in expresion:
        if caracter.isdigit() or caracter.isalpha():
            salida.append(caracter)
        elif caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Eliminar '(' de la pila
        else:  # Es un operador
            while (pila and precedencia(pila[-1]) >= precedencia(caracter)):
                salida.append(pila.pop())
            pila.append(caracter)
    
    while pila:
        salida.append(pila.pop())
    
    return ' '.join(salida)

def InfijoPostfijo():
    for i in range(len(tablita)):
        if(tablita[i].expresiones != None):
            pila = tablita[i].expresiones            
            if(pila.__contains__("+") or pila.__contains__("-") or pila.__contains__("*") or pila.__contains__("/") or pila.__contains__("^")):
                infijo = ''.join(pila)
                prefijo = infijo_a_prefijo(infijo)
                tablita[i]. expresiones = prefijo
            else: 
                continue
                        
                    

def RealcionarIDS():    
    for i in range(len(tablita)):
        
        if(tablita[i].tipo == 'ID' and tablita[i].expresiones != None):
            
            posicionID = tablita[i].pos
            expresionTemp = tablita[i].expresiones
            
            for i in range(posicionID + 1 ,len(tablita)):
                
                if(tablita[i].tipo == 'ID' and tablita[i].expresiones == None and tablita[posicionID].lexema == tablita[i].lexema):
                    
                    tablita[i].expresiones = expresionTemp
                    
                if(tablita[i].expresiones != None and tablita[posicionID].lexema == tablita[i].lexema):
                    break

def Estadefinido():
    for i in range(len(tablita)):
        if(tablita[i].expresiones == None and tablita[i].tipo == 'ID'): 
            print("El ID: " + tablita[i].lexema + " no esta definido")
            sys.exit()              


def CrearArbol():
    for i in range(len(tablita)):
                  
        if(tablita[i].tipo == 'ID' and  tablita[i].expresiones != None ):
             
            if(tablita[i].expresiones > 0):
                pila = tablita[i].expresiones
                raiz = None
             
                for i2 in range(len(pila)):
                    
                    if(raiz == None):
                        raiz = Nodo(pila[i],None,None)
                        
                        
                        
            else:
                continue                        

        else:
            
            continue
                    
                 
     

             
           
    
  

#-------------------------------------------------------------------------------------------------- 
AgregarExpresionesatabla()
InfijoPostfijo()
RealcionarIDS()
#Imprimirtabla()
#Estadefinido()
DetectarExpresiones()



        
                    

                        
                
                
        