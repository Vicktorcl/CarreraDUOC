import os

os.system("cls")
print("\n---------------Ejemplo 1------------------")

verduras=["zanahoria","tomate","palta"]

print(verduras) #imprimimos como un TODO la lista

for k in verduras: # imprimimos cada valor
    print (k)
    
print(f"El valor del 2do elemento es {verduras[1]}")

print("\n Ahora vamos a agregar un nuevo elemento")
verduras.append("papas")

print(verduras)

print('''\n Podemos insertar un elemento en
      una posición determinada usando insert ''')
verduras.insert(1,"lechuga")
print(verduras)

print('''\n podemos eleminar un elemento usando pop''')
verduras.pop(3)  #---> pop pide posición!!!!!
print(verduras)