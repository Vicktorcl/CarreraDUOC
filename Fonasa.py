import os
from string import printable
#------------ VARIABLES ------------
opcion_menu=""
rut=""
lista_rut=[]
nombre=""
lista_nombres=[]
direccion=""
lista_direcciones=[]
correo=""
lista_correos=[]
edad=0    #----> número entero entre 0 y 110
lista_edad=[]
Sexo=""   #---> F o M
lista_sexo=[]
celular=""
lista_celulares=[]
registro=""
lista_registro=[]
isapre=""
lista_isapre=[]
fecha=""
lista_fecha=[]
observacion=""
lista_observacion=[]
#------------ CÓDIGO PRINCIPAL ------------

while True:
    os.system("cls")
    opcion_menu=str(input('''
    -----------Centro Médico DUOC---------------

    1.	Registrar Paciente 
    2.	Atención Paciente 
    3.	Consultar Datos Paciente 
    4.	Salir

    
    Elija opción: '''))
    
    if opcion_menu=="1":
        os.system("cls")
        print("\n--------Registrar Paciente----------")
        rut= str(input("Ingrese rut sin digito verificador: ")).strip()
        while not len(rut)>0:
            print("Error...no puede estar vacioo")
            rut= str(input("Ingrese rut sin digito verificador: ")).strip()
        # dentro del rango de 5000000 y 99999999
        rut_num = int(rut)
        while not 5000000<=rut_num<=99999999:
            print("Error fuera de rango 5MM a 99MM")
            rut= str(input("Ingrese rut: ")).strip()
            rut_num = int(rut)
        lista_rut.append(rut)
        
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error...no puede estar vacio")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        lista_nombres.append(nombre)
        
        direccion=str(input("Ingrese dirección: ")).strip()
        while not len(direccion)>0:
            print("Error...no puede estar vacio")
            direccion=str(input("Ingrese dirección: ")).strip()
        lista_direcciones.append(direccion)
        
        correo=str(input("Ingrese correo: ")).strip().lower()
        while not "@" in correo:
            print("Error correo debe tener arroba!")
            correo=str(input("Ingrese correo: ")).strip().lower()
        lista_correos.append(correo) 
         
        edad = int(input("Ingrese edad: "))    
        while not 0<=edad<=110:
            print("Error, fuera rango[0 a 110] ")
            edad = int(input("Ingrese edad: "))
        lista_edad.append(edad)    
        
        sexo=str(input("Ingrese genero: F/M ")).strip().upper()
        while not sexo in ["F", "M"]:
            print("Error, debe ser F o M")
            sexo=str(input("Ingrese genero: F/M ")).strip().upper()
        lista_sexo.append(sexo)    
        
        registro=str(input("Ingrese el registro del paciente: ")).strip().capitalize()
        while not len(registro)>0:
            print("Error...no puede estar vacio")
            registro=str(input("Ingrese el registro del paciente: ")).strip().capitalize()
            lista_registro.append(registro)
        
        isapre=str(input("Ingrese si pertenece a isapre o fonasa: ")).strip().capitalize()
        while isapre not in ["Isapre","Fonasa"]:
            print("Error, es Isapre o fonasa")
            isapre=str(input("Ingrese si pertenece a isapre o fonasa: ")).strip().capitalize()
        lista_isapre.append(isapre)
        os.system("pause")
        
    if opcion_menu=="2":
        os.system("cls")
        print("\n----Atención Paciente----")
        rut=str(input("Ingrese rut sin digito verificador: ")).strip()
        while not len(rut)>=8:
            print("Error....ingrese rut sin digito ni puntos")
            rut=str(input("Ingrese rut: ")).strip()
        
        if rut not in lista_rut:
            print("RUT no esta registrado")
        else:
            k = lista_rut.index(rut)
            os.system("cls")
            print(f''' \n
            --------El paciente esta registrado--------------      
            ''')
            os.system("cls")
            
            fecha= str(input("Ingrese fecha de consulta dd/mm/aaaa: "))
            while not len(fecha)>0:
                print("Error...no puede estar vacio")
                fecha= str(input("Ingrese fecha de consulta dd/mm/aaaa: "))
                
                
            observacion=str(input("Ingrese observacion: ")).strip().capitalize()
            while not len(observacion)>0:
                print("Error...no puede estar vacio")
                observacion=str(input("Ingrese observacion: ")).strip().capitalize()
            registro2=fecha  + registro  + observacion
            lista_registro.append(registro2)
            
        
        
        os.system("pause")
        
    if opcion_menu=="3":
        os.system("cls")
        print("\n-------------Consultar datos del paciente-----------")
        rut=str(input("Ingrese rut: ")).strip()
        while not len(rut)>=8:
            print("Error....ingrese rut sin digito ni puntos")
            rut=str(input("Ingrese rut: ")).strip()
        
        if rut not in lista_rut:
            print("RUT no esta registrado")
        else:
            k = lista_rut.index(rut)
            os.system("cls")
            print(f''' \n
            ---------------------FICHA-----------------      
            \t Rut:{lista_rut[k]}   \t Nombre:{lista_nombres[k]}
            \t Edad: {lista_edad[k]} \t  Sexo:{lista_sexo[k]}
            \t Correo{lista_correos[k]} \t Dirección: {lista_direcciones[k]}
            \t Isapre:{lista_isapre[k]} 
            \t Registro:{lista_registro[k]}
            -------------------------------------------      
            \n    ''')
        
        
        os.system("pause")
        
    if opcion_menu=="4":
        salir=input("Desea salir del sistema S/N: ").strip().capitalize()
        if salir=="S":
            break