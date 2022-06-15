import os
from tkinter import Menu
#--------------------------- VARIABLES -----------------------------
opcion_menu=""
codigo=""        # SOlO 3 CARACTERES
lista_codigos=[]
nombre=""
pais_origen=""
lista_nombres=[]
precio=0         # debe ser mayor a cero
lista_precios=[]
estilo=""        # puede ser "Frutal", "Ale" o "Amber"
lista_estilos=[]
lista_pais_origen=[]
abv=0            # debe ser mayor o igual a cero
lista_abv=[]
observacion=""
lista_observaciones=[]
#------------------------CÓDIGO PRINCIPAL---------------------------
while True:
    os.system("cls")
    opcion_menu=str(input(''' 
    -----------APP CERVECERA-------
    1. Registrar cerveza 
    2. Listar cervezas
    3. Buscar cerveza por código
    4. Eliminar registro cerveza
    5. Modificar registro cerveza
    6. Buscar cervezas por estilo
    7. Ingresar observaciones a cerveza
    8. Salir
    
    Elija opción:   '''))
        
    if opcion_menu=="1":
        os.system("cls")
        print("\n----------Registrar Cerveza------------")
        codigo=str(input("Ingrese código: ")).strip().upper()
        while not len(codigo)==3:
            print("Error... Deben ser 3 caracteres minimo")
            codigo=str(input("Ingrese código: ")).strip().upper()
        lista_codigos.append(codigo)
        
        nombre=str(input("Ingrese nombre:  ")).strip().capitalize()
        while not len(nombre)>0:
            nombre=str(input("Ingrese nombre:  ")).strip().capitalize()
        lista_nombres.append(nombre)
        
        precio=int(input("Ingrese Precio $"))
        while not precio>0:
            print("Error... Debe ser mayor a cero")
            precio=int(input("Ingrese Precio $"))
        lista_precios.append(precio)
        
        pais_origen=str(input("Ingrese país de origen: ")).strip().capitalize()
        while not len(pais_origen)>0:
            print("Error... no puede ser vacio")
            pais_origen=str(input("Ingrese país origen: ")).strip().capitalize()
        lista_pais_origen.append(pais_origen)
        
        estilo=str(input("Ingrese estilo: ")).strip().lower()
        while estilo not in ["frutal", "ale", "amber"]:
            print("Error, puede ser Frutal, Ale o Amber")
            estilo=str(input("Ingrese estilo: ")).strip().lower()
        lista_estilos.append(estilo)
        
        abv=float(input("Ingrese AVB: "))
        while not abv>=0:
            print("Error... Debe ser mayor o igual a cero")
            abv=float(input("Ingrese AVB: "))
        lista_abv.append(abv)
        
        op=str(input("¿Desea ingresar observacion? S/N ")).upper()
        if op=="N":
            lista_observaciones.append("Sin observacón")
        else:
            fecha = str(input("Ingrese fecha: dd/mm/aaaa   "))
            obs=str(input("Ingrese observación: ")).strip
            observacion=f'''
            Fecha: {fecha}
            {obs}
            '''
            lista_observaciones.append(observacion)
        
        print("\n................Registro Finalizado.....................\n")
        
        os.system("pause")
        
        
    if opcion_menu=="2":
        os.system("cls")
        print("\n------------Listar Cervezas-------------")
        for k in range(len(lista_nombres)):
            print(f'''
            {lista_nombres[k]} {lista_abv[k]} % {lista_observaciones[k]}
            ''')
        
        
    
    if opcion_menu=="8":
        break
        