import os
#---------VARIABLES-----------
opcion_menu=""
codigo=""
lista_codigos=[]
nombre=""
lista_nombres=[]
precio=0
lista_precios=[]
pais_origen=""
lista_pais_origen=[]
estilo=""
lista_estilos=[]
avb=0
lista_avb=[]
observacion=""
lista_observaciones=[]

#---------CÓDIGO PRINCIPAL-----------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    -------MENÚ-------
    1.- Registrar cerveza
    2.- Listar cervezas
    3.- Buscar cerveza por código 
    4.- Eliminar registro cerveza
    5.- Modificar registro cerveza
    6.- Buscar cervezas por estilo
    7.- Ingresar observaciones a cerveza 
    8.- Salir
                      
    Ingrese opción:   '''))
    
    if opcion_menu=="1":        
        os.system("cls")
        print("\n-----REGISTRAR CERVEZA---------")
        codigo=str(input("Ingrese código: ")).strip().upper()
        while not len(codigo)==3:
            print("Error..debe ser 3 caracteres")
            codigo=str(input("Ingrese código: ")).strip().upper()
        lista_codigos.append(codigo)    
        
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error..no puede ser vacio")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        lista_nombres.append(nombre)
        
        precio=int(input("Ingrese precio $"))
        while not precio>0:
            print("Error..debe ser mayor a cero")
            precio=int(input("Ingrese precio $"))
        lista_precios.append(precio)    
        
        pais_origen=str(input("Ingrese país origen: ")).strip().capitalize()
        while not len(pais_origen)>0:
            print("Error..no puede ser vacio")
            pais_origen=str(input("Ingrese país origen: ")).strip().capitalize()
        lista_pais_origen.append(pais_origen)    
            
        estilo=str(input("Ingrese estilo: ")).strip().lower()
        while estilo not in ["frutal","ale", "amber"]:
            print("Error..solo permite: frutal, ale o amber")
            estilo=str(input("Ingrese estilo: ")).strip().lower()
        lista_estilos.append(estilo)    
            
        avb=float(input("Ingrese avb:  "))
        while not avb>=0:
            print("Error..no puede ser negativo")
            avb=float(input("Ingrese avb:  "))
        lista_avb.append(avb)    
        
        op=str(input("¿Desea agregar observación? S/N")).strip().upper()
        if op=="S":
            fecha=str(input("Ingrese fecha dd/mm/aaaa:  "))
            observacion=str(input("Ingrese observacion: "))
            obs= f'''
                ------------OBS-----------
                Fecha: {fecha}
                Observación: {observacion}
                 '''
        else:
            obs="Sin observación"    
        lista_observaciones.append(obs)    
        os.system("pause")
        
    if opcion_menu=="2":
        os.system("cls")
        for k in range(len(lista_codigos)):
            print(f'''
            {lista_nombres[k]} {lista_avb[k]}%
            ''')
        os.system("pause")
        
    if opcion_menu=="3":
        os.system("cls")
        print("\n------BUSCAR POR CODIGO--------")
        codigo=str(input("Ingrese codigo: ")).strip().upper()
        while not len(codigo)==3:
            print("Error... debe tener 3 caracteres")
            codigo=str(input("Ingrese codigo: ")).strip().upper()
            
        # VAMOS A CONSULTAR SI ESTA CONTENIDO EN EL CODIGO
        if codigo not in lista_codigos:
            print("NO ESTA EL REGISTRO!!!")
        else:
            # SI esta el código y ahora necesitamos
            # determinar la posición(index) del código
            k = lista_codigos.index(codigo)
            print(f'''
            {lista_nombres[k]} {lista_avb[k]}%
                 ''')
        os.system("pause")
        
    if opcion_menu=="4":
        os.system("cls")
        print("\n------ELIMINAR POR CODIGO--------")
        codigo=str(input("Ingrese codigo: ")).strip().upper()
        if codigo not in lista_codigos:
            print("NO ESTA EL REGISTRO!!!")
        else:
            # Nos interesa el index (posición)
            k= lista_codigos.index(codigo)
            # extraemos los elementos de las listas
            lista_codigos.pop(k)
            lista_nombres.pop(k)
            lista_avb.pop(k)
            lista_pais_origen.pop(k)
            lista_precios.pop(k)
            lista_observaciones.pop(k)
            lista_estilos.pop(k)
            print("\n....registro eliminado....")
        os.system("pause")
        
    if opcion_menu=="5":
        os.system("cls")
        print("\n------BUSCAR POR CODIGO--------")
        codigo=str(input("Ingrese codigo: ")).strip().upper()
        
        # VAMOS A CONSULTAR SI ESTA CONTENIDO EL CODIGO
        if codigo not in lista_codigos:
            print("NO ESTA EL REGISTRO!!!")
        else:
            k= lista_codigos.index(codigo)
            lista_nombres[k]=str(input("Ingrese nombre: "))
            lista_precios[k]=int(input("Ingrese precio $"))
            lista_avb[k]=float(input("Ingrese avb: "))
            lista_pais_origen[k]=str(input("Ingrese pais origen: "))
            lista_estilos[k]=str(input("Ingrese estilo: "))
            print("\n...registro modificado.......")
        os.system("pause")
        
    if opcion_menu=="6":
        os.system("cls")
        print("\n--------BUSCAR POR ESTILO-------")
        estilo=str(input("Ingrese estilo: ")).strip().lower()
        encontrado=False
        for k in range(len(lista_codigos)):
            if lista_estilos[k]==estilo:
                print(f'''
                {lista_nombres[k]} {lista_avb[k]}%
                ''')
                encontrado=True
        if encontrado==False:
            print("No hay registro de tal estilo!!")           
        os.system("pause")
        
    if opcion_menu=="7":
        os.system("cls")
        
        os.system("pause")
        
    if opcion_menu=="8":
        break
     