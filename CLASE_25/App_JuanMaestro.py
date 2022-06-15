import os
#-----------------------------------VARIABLES------------------------------------
rut=0            #entre 4MM y 99MM
lista_rut=[]
nombre=""
lista_nombre=[]
direccion=""
lista_direccion=[]
comuna=""
lista_comuna=[]
correo=""       # Debe tener arroba @
lista_correo=[]
edad=0         #Entre 0 y 110
lista_edad=[]
genero=""    # F o M
lista_genero=[]
celular=0
lista_celular=[]
tipo=""         # Solo puede ser premiun, gold o silver
lista_tipo=[]
suscripcion=""
lista_suscripcion=[]
opcion_menu=""
#--------------------------------CODIGO PRINCIPAL-------------------------------------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    -----------MENU---------
    -------Juan Maestro App------------- 
    1.Registrar Cliente 
    2.Suscripción 
    3.Consultar Datos Cliente 
    4Salir '''))
    if opcion_menu==1:
        os.system("cls")
        print("\n---------INGRESO DATOS--------")
        rut=str(input("Ingrese rut ")).strip()
        # vamos a validar en forma númerica
        rut_num = int(rut)
        while not 4000000<=rut_num<=99999999:
            print("Error... rango 4MM a 99MM")
            rut=str(input("Ingrese rut ")).strip()
            rut_num = int (rut)
        lista_rut.append(rut)
        
        nombre=str(input("Ingrese nombre ")).strip()
        os.system("pause")
    if opcion_menu==2:
        os.system("cls")
        os.system("pause")
    if opcion_menu==3:
        os.system("cls")
        os.system("pause")
    if opcion_menu==4:
        break