import os
#------------------ Variables ---------------------
opcion_menu=""
run="0"
lista_run=[]
nombre=""
lista_nombre=[]
edad=0
lista_edades=[]
#------------------ CÓDIGO PRINCIPAL ------------------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    ------ MENÜ --------
    1.- Agregar usuario
    2.- Listar usuarios
    3.- Buscar usuario por run
    4.- Salir
    
    Elija opción:       '''))
    
    if opcion_menu=="1":
        os.system("cls")
        print("n\---- Agregar Usuario -----")
        # solicitas dato al user... limpias espacios
        run= str(input("Ingrese run: ")).strip()
        # validr dato... "while not" Regla
        while not len(run)>0:
            print("Error... No puede ser vacio")
            run= str(input("Ingrese run: ")).strip()
        # una vez validado el dato lo agregamos
        # a la lista correspondiente
        lista_run.append(run)
        # para comnentar CONTROL + }
        edad=int(input("Ingrese su edad"))
        while not 18<=edad<=100:
            print("Error... fuera del rango de edad 18 a 100")
            edad=int(input("Ingrese edad: "))
        lista_edades.append(edad)
        
        # para ajustar el código a la pantalla
        # presiona ALT + Z
        
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        
        while not len(nombre)>0:
            print("Error... no puede ser vacio")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
    
        lista_nombre.append(nombre)
        # visualizamos datos
        print(f'''
        {lista_run}
        {lista_nombre}
        {lista_edades}''')
        os.system("pause")
        
    if opcion_menu=="2":
        os.system("cls")
        os.system("cls")
        print("\n---- Listar Usuarios --------")
        # len(lista) ---> det. la cantidad de elementos
        # range(n) ---> 0 hasta N-1
        for k in range(len(lista_run)):
            print(f'''
            {lista_run[k]} {lista_nombre[k]} {lista_edades[k]} años
            ''')
        
        os.system("pause")
        
    if opcion_menu=="3":
        os.system("cls")
        print("\n------ Buscar por run -------")
        run=str(input("Ingrese run: ")).strip()
        if run not in lista_run:
            print("No esta registrado este run")
        else:
            k= lista_run.index(run)
            print(f'''
            {lista_nombre}[k] {lista_edades}[k]
            ''')
        
        os.system("pause")
        
    if opcion_menu=="4":
        op=str(input("¿Estas seguro de salir? S/N ")).upper()
        
        if op=="S":
            break
        