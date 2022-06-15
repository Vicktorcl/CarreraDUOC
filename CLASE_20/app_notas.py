import os
#------------------------variables----------------------------
Opcion_menu=""
nota1=0
nota2=0
nota3=0
promedio=0
estado=""
cant_alumno_atendidos=0
cant_alumnos_aprobados=0
cant_alumnos_reprobados=0
#-------------------código principal--------------------------

while True:
    os.system("cls")
    Opcion_menu=str(input('''
    --------------Menú--------------
    1.- Calcular promedio
    2.- Ver estadisticas
    3.- Salir
    
    Elija opción:          '''))
    
    if Opcion_menu=="1":
        os.system("cls")
        print("\n--- Calcular Promedio -----")
        nota_1=float(input("Ingrese su primera nota: "))
        nota_2=float(input("Ingrese su segunda nota: "))
        nota_3=float(input("Ingrese su tercera nota: "))
        
        promedio=(nota_1+nota_2+nota_3)/3
        if promedio>=4:
            estado="APROBADO"
            cant_alumnos_aprobados=cant_alumnos_aprobados+1
        else:
            estado="REPROBADO"
            cant_alumnos_reprobados=cant_alumnos_reprobados+1
            
        cant_alumno_atendidos=cant_alumno_atendidos+1
        
        os.system("cls")
        print(f'''
        Nota1 {nota_1} \ Nota2 {nota_2} \t Nota3 {nota_3}
        Promedio: {promedio} \t Estado:{estado}
            ''')
        
        
        os.system("pause")
        
    if Opcion_menu=="2":
        os.system("cls")
        print("\n--- Ver Estadisticas  ----")
        print(f'''
            Cant. aprobados {cant_alumnos_aprobados}
            Cant. reprobados {cant_alumnos_reprobados}
            Cant. atendidos {cant_alumno_atendidos}
            ''')
        
        os.system("pause")
        
    if Opcion_menu=="3":
        op=str(input("¿Estás seguro de salir? S/N ")).upper()
        if op=="S":
            break