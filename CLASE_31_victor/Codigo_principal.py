from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
import os
import numpy as np
import Funciones_empleados as fe
#--------------------- VARIABLES ------------------------
opcion_menu=""         # Selección del usuario
tamaño=3               # cant. max. de empleados
ruts= np.empty(tamaño, dtype=object)
nombres= np.empty(tamaño, dtype=object)
sueldos_brutos= np.empty(tamaño, dtype=int)
sueldos_liquidos= np.empty(tamaño, dtype=float)
#------------------------ CÓDIGO PRINCIPAL --------------------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    ----------- APP Empleados ---------
    
    1.Cargar datos y ver liquidación
    2.Ver estadisticas
    3.Salir 
    
    
    Elija opción:'''))
    if opcion_menu=="1":
        os.system("cls")
        print("\n--------CARGAR DATOS--------")
        for k in range(tamaño):
            ruts[k]= str(input("Ingrese rut: ")).strip()
            while not len(ruts[k])>0:
                print("Error no puede estar vacío ")
                ruts[k]= str(input("Ingrese rut: ")).strip()
            
            nombres[k]=str(input("Ingrese nombre: ")).strip()
            while not len(nombres[k])>0:
                print("Error no puede estar vacío ")
                nombres[k]=str(input("Ingrese nombre: ")).strip()
            
            sueldos_brutos[k]=int(input("Ingrese sueldo bruto $"))
            while not sueldos_brutos[k]>0:
                print("Error no puede estar vacío ")
                sueldos_brutos[k]=int(input("Ingrese sueldo bruto $"))
            
            # ahora enviamos los parámetros a nuestras funciones
            # las cuales nos van a retornar 3 datos
            salud, pension, liquido = fe.calcular_descuentos_legales(sueldos_brutos[k])
            (sueldos_brutos[k])
        
            sueldos_liquidos[k]=liquido
        
            fe.imprimir_liquidacion(ruts[k], nombres[k], sueldos_brutos[k],salud, pension, liquido)
            os.system("pause")
            os.system("cls")
    if opcion_menu=="2":
        os.system("cls")
        print("\n---------------- ESTADISTICAS -----------------")
        fe.determinar_sueldo_max(ruts, nombres, sueldos_liquidos)
        os.system("pause")
    if opcion_menu=="3":
        break