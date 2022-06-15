import random
import os

#-------------------- definimos variables ----------------------------------
numero_secreto= random.randint(1, 20)  # ----> numero aleatorio entre 0 y 20
intentos=5  #--> cantidad max de intentos
distancia=0  #-> Que tan lejos se encuentra del valor a adivinar
apuesta=0  #--> numero que el usuario apuesta que es el secreto


#-------------------- Código Principal  ----------------------------------
os.system('cls')
print("Bienvenido a pseudo Toque y Fama v1.0    ")
print("Debera intentar adivinar un numero secreto entre 0 y 20\n\n\n")
os.system("pause")


while True:
    

    if intentos==0:
        break
    
        

    print(f"\n\nUsted disponde {intentos} intentos \n\n")
    apuesta=int(input("Ingrese su apuesta  "))
    # sacamos el valor absoluto entre el numero secreto y la apuesta para
    # determinar que tan lejos esta del numero secreto
    distancia=abs(apuesta-numero_secreto)
    if distancia==0:
        print("FAMA!!!! acertaste!!! ")
        break
    if distancia>2:
        print("LEJOS....")
        
    if distancia==2:
        print("CERCA....")
    if distancia==1:
        print("MUuuuy Cerca...")
    
    intentos=intentos-1  # es lo mismo que   intentos=intentos-1
    
print(f"\n\n\nEl numero secreto {numero_secreto}")



    