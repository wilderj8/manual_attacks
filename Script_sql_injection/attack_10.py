"""
Conocida cómo shebang o hashbang, quiere decir que el interprete del código sea python3.
"""
#!/usr/bin/python3 

"""
LIBRERIAS
[pwn]: Importa (*) todas las funciones y clases de la librería. Incluye conexiones de red, manipulación de datos binarios,
creación de archivos shellcode, creación de payloads maliciosos

[requests]:Sirve para enviar solicitudes HTTP através de la red.

[signal]:Sirve para interactuar con señales del sistema operativo.

[time]:Sirve para trabajar con el tiempo y las fechas.

[pdb]:Sirve para depurar el código.

[sys]:Sirve para interactuar con el interprete de python y el sistema operativo principal.

[string]:Sirve para modificar y trabajar con cadenas de texto.
"""
from pwn import * 
import requests, signal, time, pdb, sys, string


"""
[def_handler]: Sirve para decir cuando seguir o cuando detenerse.

[sig]: Es la señal que activo la función.

[SIGINT]: Cuando el usuario presiona ctrl+c.

[frame]: Es como el que sabe donde está todo.
"""


def def_handler(sig,frame):
    print("\n\n[!] saliendo.... \n") #[\n]: Crean una nueva linea
    sys.exit(1) #Indicamos que estamos forzando al programa para que termine


#Debemos saber el número límite de la contraseña paso #6.2.1.2
numero_límite_de_la_contraseña=0

def crear_petición():
    signal.signal(signal.SIGINT, def_handler)
    url_principal="https://pegar:el_url_principal" #Hay que agregarle [https://]
    caracteres=string.ascii_lowercase+string.digits
    #for posicion in range(1,numero_límite_de_la_contraseña):
        
    



#if __name__=='__main__':
 #   crear_petición()