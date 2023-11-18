#Librerias


def guardar_variable(variable1,variable2):# Guardar la variable en un archivo
    with open("borrador.txt", "w") as archivo:
        archivo.write(str(variable1)+","+variable2)#Hay que separa las variables cuando se guarden [","]


def recuperar_variable():# Recuperar la variable del archivo
    with open("borrador.txt", "r") as archivo:
        contenido = archivo.read()

    valores=contenido.split(",")
    return valores



def menu_principal():#menu principal
    tipo_de_ataque="" 
    numero_de_ataque=0

    #Logo de bienvenida
    print()
    print("     WELCOME TO MANUAL ATTACKS ")
    print("█████████████████████████████████")
    print("     ▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒")
    print("     ▒▒█▒▒▒▄██████████▄▒▒▒▒")
    print("     ▒█▐▒▒▒████████████▒▒▒▒")
    print("     ▒▌▐▒▒██▄▀██████▀▄██▒▒▒")
    print("     ▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒")
    print("     ▐┼▐▒▒██████████████▒▒▒")
    print("     ▐▄▐████─▀▐▐▀█─█─▌▐██▄▒")
    print("     ▒▒█████──────────▐███▌")
    print("     ▒▒█▀▀██▄█─▄───▐─▄███▀▒")
    print("     ▒▒█▒▒███████▄██████▒▒▒")
    print("     ▒▒▒▒▒██████████████▒▒▒")
    print("     ▒▒▒▒▒█████████▐▌██▌▒▒▒")
    print("     ▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒")
    print("     ▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒")
    print("█████████████████████████████████")
    print()

    #hablamos de las reglas
    print("Rules:")
    print("Rule #1: Los simbolos [] quiere decir ahí es donde tenemos que modificar para hacer el ataque. ")

    #Recuperamos datos de la última vez que ejecutamos el programa
    contenido_borrador_txt=recuperar_variable()
    numero_de_ataque=contenido_borrador_txt[1]
    tipo_de_ataque=contenido_borrador_txt[0]
    
    #Mostramos los últimos movimientos que se hicieron
    print(f"Last hit --> type of attack:{tipo_de_ataque}  number of the attack:{numero_de_ataque}")

    #Menu de selección de ataque
    print("ATTACKS")
    print("-->[1] SQL Injection")
    print("-->[$] Select last hit")
    print()
    select_option=input("select: ")
    print()
    if(select_option=="$"):
        if(tipo_de_ataque=="sql_inyection"):
            import sql_inyection
            sql_inyection.content_sql_injection(numero_de_ataque)                
    elif(select_option == "1"):
        import sql_inyection
        sql_inyection.sql_injection_menu()        

