import os
import numpy as np 
#------------------------VARIABLES--------------------
opcion_menu=""   # Selección del usuario
# vamos a crear los arreglos que contendra info
tamaño=3 #--> fijamos el largo del arreglo
nombres= np.empty(tamaño, dtype=object)
edades= np.empty(tamaño, dtype=int)
sexo= np.empty(tamaño, dtype=object)
sueldos=np.empty(tamaño, dtype=int)

#------------------CODIGO PRINCIPAL---------------------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    ---------APP Empleados---------
    1.- Cargar datos
    2.- Listar todos los empleados
    3.- Estadisticas
    4.- Salir                      
    
    Elija opción: '''))
    
    if opcion_menu=="1":
        os.system("cls")
        print("\n--Cargar Datos---")
        for k in range(tamaño):
            nombres[k]=str(input("Ingrese nombre: ")).strip()
            while not len(nombres[k])>0:
                print("Error No puede estar vacío!!")
                nombres[k]=str(input("Ingrese nombre: ")).strip()
                
            edades[k]=int(input("Ingrese edad: "))
            while not edades[k]>=18:
                print("Error la edad tiene que ser igual o mayor a 18 ")
                edades[k]=int(input("Ingrese edad: "))
            
            sexo[k]=str(input("Ingrese su genero F/M ")).strip().upper()
            while sexo[k] not in ["F", "M"] :
                print("Error solo puede ser F o M")
                sexo[k]=str(input("Ingrese su genero F/M ")).strip().upper()
                
            sueldos[k]=int(input("Ingrese sueldo $"))
            while not sueldos[k]>0:
                print("Error tiene que ser mayor a cero")
                sueldos[k]=int(input("Ingrese sueldo $"))
                
            print(f'''
            se registro...
            Nombre:{nombres[k]} \t Edad:{edades[k]}
            Sexo:{sexo[k]} \t Sueldo ${sueldos[k]}  ''')
            os.system("pause")
            os.system("cls")
            
        os.system("pause")
    if opcion_menu=="2":
        os.system("cls")
        print("\n--Listar Datos---")
        for k in range(tamaño):
            print(f'''
            -------------------Empleado {k+1}------------------
            Nombre:{nombres[k]} \t Edad:{edades[k]}
            Sexo:{sexo[k]} \t Sueldo ${sueldos[k]}             
            ''')
        
        os.system("pause")
    if opcion_menu=="3":
        os.system("cls")
        min_sueldo = sueldos.min()
        max_sueldo = sueldos.max()
        prom_sueldo = sueldos.mean()
        print(f'''
        ---------------Estadísticas------------
        Sueldos>>>> min ${min_sueldo} max ${max_sueldo}
                    Promedio ${prom_sueldo}
                    ''')
        os.system("pause")
    if opcion_menu=="4":
        break