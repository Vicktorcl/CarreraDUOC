import os
#Vamos a emular una pequeña base de datos usando listas
#-----------------------variables------------------------
opcion_menu=""
nombre=""
lista_nombres=[]
edad=0
lista_edades=[]
sexo="" #
lista_sexo=[]
sueldo=0
lista_sueldo=[]
#------------------Codigo Principal---------------------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    ---------MENÚ---------
    1.- Cargar datos
    2.- Listar datos
    3.- Salir
    
    Ingrese opción:   '''))
    
    if opcion_menu=="1":
        os.system("cls")
        print("\n-----------CARGAR DATOS-------------")
        nombre= str(input("Ingrese nombre: ")).strip()
        while not len(nombre)>0:
            print("Error... No puede estar vacio")
            nombre= str(input("Ingrese nombre: ")).strip()
        lista_nombres.append(nombre)
        
        
        edad= int(input("Ingrese edad: "))
        while not 18<=edad<=100:
            print("Error... Valor valido solo entre 18 y 100 años")
            edad= int(input("Ingrese edad: "))
        lista_edades.append(edad)
        
        
        sexo= str(input("Ingrese su genero: F/M ")).upper()
        while sexo not in ["F", "M"]:
            print("Error... Solo se puede ingresar F o M")
            sexo= str(input("Ingrese su genero: F/M ")).upper()
        lista_sexo.append(sexo)
        
        sueldo=int(input("Ingrese sueldo $"))
        while not sueldo>=340000:
            print("Error... Sueldo minimo $340000")
            suelo=int(input("Ingrese sueldo $"))
        lista_sueldo.append(sueldo) 
        print(f'''
            {lista_nombres}
            {lista_edades}
            {lista_sexo}
            {lista_sueldo}
            ''')
        os.system("pause")
    
    if opcion_menu=="2":
        os.system("cls")
        print("\n------------ LISTAR DATOS --------")
        for k in range(len(lista_nombres)):
            print(f'''
            {lista_nombres[k]} {lista_edades[k]} años
            {lista_sexo[k]}     {lista_sueldo[k]} $
            ''')
        
        os.system("pause")
        
    if opcion_menu=="3":
        break
        # nombre edad años
        # Pablo  26 años