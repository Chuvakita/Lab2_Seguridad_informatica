#Laboratorio 2 seguirdad informática
#Diego González
#José Ochoa
#Ignacio Henríquez
#Programa para encriptar
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

def leer_mensaje(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()
    contador = 0
    while contador < len(lineas):
        lineas[contador] = lineas[contador].strip().split("	")
        contador += 1
    mensaje = lineas[0][0]
    archivo.close()
    return mensaje

    
#Función para escribir cifrado
def escribirArchivo(nombre_archivo,cifrado,Hash):
    archivo = open(nombre_archivo, "w")
    archivo.write(cifrado+"	"+Hash+"\n")
    archivo.close()

abc = leer_caracteres("caracteres.txt")
abc2 = leer_caracteres("caracteres.txt")

def main():
    
        
    clave = "contrasenasecreta"
    clave2 = "atercesanesartnoc"
    c = leer_mensaje("mensajedeentrada.txt")
    print(c)
    bdatos = bytes(c, "utf-8")
    h = hashlib.new("sha256", bdatos)
    hash1= HASH.generarHash(h)
    print(hash1)
    rot16 = rot(c,16)
    rot24 = rot(rot16,24)
    vig = vigerente(rot24,clave)
    rot32 = rot(vig,32)
    rot64 = rot(rot32,64)
    cifrado = vigerente(rot64,clave2)
    print(cifrado)
    escribirArchivo("mensajeseguro.txt",cifrado,hash1)
    print(" ")
    print("Mensaje encriptado")
    
        


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

