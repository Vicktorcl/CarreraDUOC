#=======================VARIABLES=========================
from re import S
import numpy as np
import os
opcion_menu=""
opcion=0
num_asiento=0
valor_asiento=0
total_tipo_b=0
total_tipo_c=0
total_tipo_a=0
total_tipo_d=0
cantidad=0
cont_cantidad=0
acum_subtotal=0
total_ventas=0
fila=0
rut=0
columna=""
prueba=fila-1
tipo_b=0
tipo_c=0
tipo_a=0
tipo_d=0
validar=True
asiento_reservado="no" 
encontrado="no"

ruts_ordenados=""

temp=0

ruts=np.empty(162,dtype=int)

a= np.empty(27,dtype=object)
b= np.empty(27,dtype=object)
c= np.empty(27,dtype=object)
d= np.empty(27,dtype=object)

#==================CODIGO PRINCIPAL============================
for k in range (0,27):
    a[k]="D"
    b[k]="D"
    c[k]="D"
    d[k]="D"

for k in range (0,162):
    ruts[k]=0

while True:
    os.system("cls")
    opcion_menu=str(input('''
    ===============MENÚ INMOVILIARIA CASA FELIZ===================
    1. Comprar departamento
    2. Mostrar departamentos disponibles
    3. Ver listado de compradores
    4. Mostrar ganancias totales
    5. Salir
    
    Ingrese opción:   '''))
    if opcion_menu=="1":        
        os.system("cls")
        print(f'''
             A    B    C    D
       |10 |[{a[10]}] |[{b[10]}] |[{c[10]}] |[{d[10]}]|
        |9  |[{a[9]}] |[{b[9]}] |[{c[9]}] |[{d[9]}]|
        |8  |[{a[8]}] |[{b[8]}] |[{c[8]}] |[{d[8]}]|
        |7  |[{a[7]}] |[{b[7]}] |[{c[7]}] |[{d[7]}]|
        |6  |[{a[6]}] |[{b[6]}] |[{c[6]}] |[{d[6]}]|
        |5  |[{a[5]}] |[{b[5]}] |[{c[5]}] |[{d[5]}]|
        |4  |[{a[4]}] |[{b[4]}] |[{c[4]}] |[{d[4]}]|
        |3  |[{a[3]}] |[{b[3]}] |[{c[3]}] |[{d[3]}]|
        |2  |[{a[2]}] |[{b[2]}] |[{c[2]}] |[{d[2]}]|
        |1. |[{a[1]}] |[{b[1]}] |[{c[1]}] |[{d[1]}]|

        [D] Disponible
        [X] Reservado 
        ''')
        print(f''' 
            |Tipo    | PRECIO | 
            |[A]     | 3800UF | 
            |[B]     | 3000UF | 
            |[C]     | 2800UF | 
            |[D]     | 3500UF |  \n\n''')
        cantidad=0
        cantidad=int(input("Ingrese cantidad de departamentos a comprar:"))
        while cantidad<1:
            print("Error no puede estar vacío")
            cantidad=int(input("Ingrese cantidad de pasajes:")) 
        cont_cantidad=0
        acum_subtotal=0
        fila=0
        
        while cont_cantidad!=cantidad:

            rut=int(input("\nIngrese rut(sin digito verificador): "))

            
            columna=input("Ingrese Columna(a-b-c-d): ").lower()
            while columna!="a" and columna!="b" and columna!="c" and columna!="d":
                columna=input("Ingrese Columna(a-b-c-d): ").lower()
                lista_columna=[]

            

            fila=int(input("Ingrese Nro. de fila: "))
            while fila<0 or fila>=10:
                fila=int(input("Ingrese Nro. de fila: "))

            if columna=="a":
                valor_asiento=3800
                tipo_a+=1
            elif columna=="b":
                valor_asiento=3000
                tipo_b+=1
            elif columna=="c":
                valor_asiento=2800
                tipo_c+=1
            elif columna=="d":
                valor_asiento=3500
                tipo_d+=1


            if columna=="a":
                for k in range (0,10):
                    if k==fila-1:
                        if a[k+1]=="D":
                            a[k+1]="X"
                            ruts[k]=rut
                            cont_cantidad+=1
                            print("El asiento ha sido reservado") 
                        else:
                            print("El asiento ya esta reservado")
                            break  
                os.system("pause")

            if columna=="b":
                for k in range (0,10):
                    if k==fila-1:
                        if b[k+1]=="D":
                            b[k+1]="X"
                            ruts[k+27]=rut
                            cont_cantidad+=1
                            print("El asiento ha sido reservado") 
                        else:
                            print("El asiento ya esta reservado")  
                            break
                os.system("pause")

            if columna=="c":
                for k in range (0,10):
                    if k==fila-1:
                        if c[k+1]=="D":
                            c[k+1]="X"
                            ruts[k+54]=rut
                            cont_cantidad+=1
                            print("El asiento ha sido reservado") 
                        else:
                            print("El asiento ya esta reservado") 
                            break 
                os.system("pause")

            if columna=="d":
                for k in range (0,10):
                    if k==fila-1:
                        if d[k+1]=="D":
                            d[k+1]="X"
                            ruts[k+81]=rut
                            cont_cantidad+=1
                            print("El asiento ha sido reservado") 
                        else:
                            print("El asiento ya esta reservado")  
                            break

            #venta

            acum_subtotal=valor_asiento+acum_subtotal
            total_ventas=total_ventas+acum_subtotal
        print("\n\n----------------VENTA----------------")
        print(f'''
        Subtotal: {acum_subtotal}
        Cantidad de pasajes: {cantidad}
            ''')
        
        os.system("pause")
        os.system("cls")
    if opcion_menu=="2":        
        os.system("cls")
        print(f'''
             A    B    C    D
       |10 |[{a[10]}] |[{b[10]}] |[{c[10]}] |[{d[10]}]|
        |9  |[{a[9]}] |[{b[9]}] |[{c[9]}] |[{d[9]}]|
        |8  |[{a[8]}] |[{b[8]}] |[{c[8]}] |[{d[8]}]|
        |7  |[{a[7]}] |[{b[7]}] |[{c[7]}] |[{d[7]}]|
        |6  |[{a[6]}] |[{b[6]}] |[{c[6]}] |[{d[6]}]|
        |5  |[{a[5]}] |[{b[5]}] |[{c[5]}] |[{d[5]}]|
        |4  |[{a[4]}] |[{b[4]}] |[{c[4]}] |[{d[4]}]|
        |3  |[{a[3]}] |[{b[3]}] |[{c[3]}] |[{d[3]}]|
        |2  |[{a[2]}] |[{b[2]}] |[{c[2]}] |[{d[2]}]|
        |1. |[{a[1]}] |[{b[1]}] |[{c[1]}] |[{d[1]}]|

        [D] Disponible
        [X] Reservado 
        ''')
        
        os.system("pause")
        os.system("cls")
    if opcion_menu=="3":        
        os.system('cls')
        print("-----LISTADO DE COMPRADORES----")
        ruts_ordenados=np.sort(ruts)
        for k in range (0,162):
            if ruts_ordenados[k]!=0:
                print(ruts_ordenados[k])
        os.system("pause")
        os.system("cls")
    if opcion_menu=="4":        
        os.system("cls")
        total_tipo_a=valor_asiento*tipo_a
        total_tipo_b= valor_asiento*tipo_b
        total_tipo_c= valor_asiento*tipo_c
        total_tipo_d= valor_asiento*tipo_d
        cantidad_total= tipo_a+tipo_b+tipo_c+tipo_d
        total_total= total_tipo_a+total_tipo_b+total_tipo_c+total_tipo_d


        print(f''' 
                                    GANANCIAS TOTALES

        Tipo de apartamento                       |   Cantidad      |        Total    |
        A            3.800UF                      |   {tipo_a}             |          {total_tipo_a}UF    |
        B            3.000UF                      |   {tipo_b}             |          {total_tipo_b}UF    |
        C            2.800UF                      |   {tipo_c}             |          {total_tipo_c}UF    |
        D            3.500UF                      |   {tipo_d}             |          {total_tipo_d}UF    |
                                                  |                 |                 |
        Total                                     |   {cantidad_total}             |          {total_total}UF    |


        ''')
        
        os.system("pause")
        os.system("cls")
    if opcion_menu=="5":
        print('''
              Nombre:Víctor 
              Apellido:Barrientos 
              Fecha: 11/07/2022''')        
        salida=input("Desea salir del sistema S/N: ").upper()
        if salida=="S":
            break