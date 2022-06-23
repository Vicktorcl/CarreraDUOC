# Esta librería tendra las funciones
# Que usaremos en la app_empleados.py
import numpy

def calcular_descuentos_legales(sueldo_bruto):
    salud = sueldo_bruto*0.07
    pension = sueldo_bruto*0.13
    liquido = sueldo_bruto-salud-pension
    
    return salud, pension, liquido

def imprimir_liquidacion(rut, nombre, sueldo_bruto, salud, pension, liquido):
    print(f''' 
    ================================ LIQUIDACIÓN ==================================      
    \t Rut:{rut} \t\t Nombre:{nombre}
    \t Sueldo Bruto ${sueldo_bruto}
    \t Dscto. Salud ${salud}
    \t Dscto. Pension ${pension}
    
    \t Liquido pagar ${liquido}
    ===============================================================================
          ''')
    
def determinar_sueldo_max(ruts, nombres, sueldos_liquidos):
    max = sueldos_liquidos.max()
    for k in range(3):
        if max==sueldos_liquidos[k]:
            print(f'''
            Rut:{ruts[k]}
            Nombre: {nombres[k]} ${sueldos_liquidos[k]}   ''')