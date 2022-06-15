from random import randrange, choice
import os
import time
opciones =["piedra", "papel", "tijeras"]

#captuamos la apuesta el usuario

while True:
    os.system("cls")
    respuesta = input("¿Desea jugar? S/N ").upper()
    if respuesta=="S":
        
        apuestaUser = input("piedra, papel, tijeras??  ")

        if apuestaUser in opciones:
            apuestaCompu= choice(opciones)
            print("user juega "+apuestaUser)
            print("Computador juega "+apuestaCompu)
            if(apuestaUser=="piedra"):
                if(apuestaCompu=="papel"):
                    print("Perdiste!!!")
                if(apuestaCompu=="tijeras"):
                    print("Ganaste!!!")
                if(apuestaCompu=="piedra"):
                    print("Empataste!!!")

            if(apuestaUser=="papel"):
                if(apuestaCompu=="papel"):
                    print("Empataste!!!")
                if(apuestaCompu=="tijeras"):
                    print("Perdiste!!!")
                if(apuestaCompu=="piedra"):
                    print("Ganaste!!!")
                
            if(apuestaUser=="tijeras"):
                if(apuestaCompu=="papel"):
                    print("Ganaste!!!")
                if(apuestaCompu=="tijeras"):
                    print("Empataste!!!")
                if(apuestaCompu=="piedra"):
                    print("Perdiste!!!")
            
            os.system("pause")
        else:
            print("Argumento inválido: Debe ser piedra, papel o tijera.")
            time.sleep(1)

    else:
        break
