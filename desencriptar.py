#Laboratorio 2 seguirdad informática
#Diego González
#José Ochoa
#Ignacio Henríquez
import requests
import hashlib



#Función para leer archivo de caracteres
def leer_caracteres(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    contador = 0
    while contador < len(lineas):
        lineas[contador] = lineas[contador].strip().split("	")
        contador += 1
    caracteres = ""
    for i in range(0,len(lineas)):
        caracter = lineas[i][2]
        caracteres += caracter
        
    archivo.close()
    return caracteres

#Función para leer archivo de cifrado
def leer_cifrado(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    contador = 0
    while contador < len(lineas):
        lineas[contador] = lineas[contador].strip().split("	")
        contador += 1
    desencriptar = [lineas[0][0],lineas[0][1]]

        
    archivo.close()
    return desencriptar
    

abc = leer_caracteres("caracteres.txt")
abc2 = leer_caracteres("caracteres.txt")

def main():    
        
    clave = "contrasenasecreta"
    clave2 = "atercesanesartnoc"
    archivo = leer_cifrado("mensajeseguro.txt")
    cifrado = archivo[0]
    hashOriginal = archivo[1]
    desvig = desvigerente(cifrado,clave2)
    desrot64 = rot(desvig,-64)
    desrot32 = rot(desrot64,-32)
    desvig2 = desvigerente(desrot32,clave)
    desrot24 = rot(desvig2,-24)
    desifrado = rot(desrot24,-16)
    bdatos = bytes(desifrado, "utf-8")
    h = hashlib.new("sha256", bdatos)
    hash1= HASH.generarHash(h)
    print("El mensaje secreto es: "+desifrado)
    print("Y el hash: "+hash1)
    print(" ")
    if(hash1 == hashOriginal):
        print("Por lo tanto el mensaje no ha sido modificado")
        
    else:
        print("El mensaje fue modificado")
    print("Hash inicial: "+hashOriginal)
        


def rot(cadena,clave):
    text_cifrado = ''
    for letra in cadena:
        suma = abc.find(letra) + clave
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])
        
    return text_cifrado
    

def vigerente(cadena,clave):
    text_cifrar = ""

    i = 0
    for letra in cadena:
        suma = abc2.find(letra) + abc2.find(clave[i % len(clave)])
        modulo = int(suma) % len(abc)
        text_cifrar = text_cifrar + str(abc2[modulo])
        i = i+1
    return text_cifrar

def desvigerente(cadena,clave):
    text_cifrar = ""

    i = 0
    for letra in cadena:
        suma = abc.find(letra) - abc.find(clave[i % len(clave)])
        modulo = int(suma) % len(abc)
        text_cifrar = text_cifrar + str(abc[modulo])
        i = i+1
    return text_cifrar


class HASH:
    def generarHash(h):
        digest = h.hexdigest()
        return digest


        
main()
