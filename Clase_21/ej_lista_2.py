notas=[]   #---> es una lista vacia

while True:
    notas.append(float(input("Ingrese nota: ")))
    
    prom=sum(notas)/len(notas)
    
    print(f'''
        Las notas: {notas}
        Promedio: {prom}
        ''')