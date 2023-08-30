#hacer el menu intermedio
#seguir con los ataques de sql injection

#Functions
# Guardar la variable en un archivo
def guardar_variable(variable1,variable2):
    with open("borrador.txt", "w") as archivo:
        archivo.write(str(variable1)+","+variable2)

# Recuperar la variable del archivo
def recuperar_variable():
    with open("borrador.txt", "r") as archivo:
        contenido = archivo.read()

    valores=contenido.split(",")

    return valores

#menu principal
def menu_prin():
    type_attack=""
    number_attack=0
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
    print("Rules:")
    print("Rule #1: Los simbolos [] quiere decir ahí es donde tenemos que modificar para hacer el ataque. ")
    valores_list=recuperar_variable()
    number_attack=valores_list[0]
    type_attack=valores_list[1]
    print(f"Last hit --> type of attack:{type_attack}  number of the attack:{number_attack}")
    print("ATTACKS")
    print("-->[1] SQL Injection")
    print("-->[$] Select last hit")
    print()
    select_option=input("select: ")
    if(select_option=="$"):
        print("ja")
    elif(select_option == "1"):
        sql_injection_menu()
        type_attack="sql injection"

    guardar_variable(type_attack,number_attack)

#menu intermedio 
def menu_inter():
    print("1 si desea ver otros ataques de está misma vulnerabilidad")
    print("2 si desea ir al menu principal")

#Attack SQL injection
def content_sql_injection(num_sel):
    if(num_sel=="1"):
        print("the origin attack")
        print("HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor[' or 1=1 -- -] ")
        print("--------------------------------------------------------------------------")
        print("Explicación:")
        print("[']: Es para cerrar la query y hacer un hueco para introducir el ataque malicioso.")
        print("[or]: Condición en la que nos va a servir para decir si esto si cumple O si esto otro cumple.")
        print("[1=1]: Se busca un TRUE por lo cual logicamente 1 es igual a 1.")
        print("[-- -]: para comentar la query faltante que quedo de la original. ")
    

def sql_injection_menu():
    print("         SQL inyection           ")
    print("             HITS                ")
    print("█████████████████████████████████")
    print("FIRST HIT #1: The origin")
    print("SECOND HIT #2: ")
    print("█████████████████████████████████")
    num_sel=input("select number of the attack: ")
    print()
    content_sql_injection(num_sel)

#main
menu_prin()
