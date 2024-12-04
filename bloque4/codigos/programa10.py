#Programa 4.10 Crear una función para que cada vez que se llame,
#dado como argumento el número ingresado por el usuario, calcule si es primo o no
#Elaborado el 15/11/2024
#Elaborado por : Evelyn Jocelyn León de Luna

import math

# Función que determina si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    
    # divisible entre 2 y raiz
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False  #Divisible, no es primo
    
    return True  # Si no fue divisible por ningún número, es primo

# Solicitar al usuario que ingrese un número
numero_usuario = int(input("Ingrese un número entre 10 y 99: "))

# Comprobar si el número es primo y mostrar el resultado
if 10 <= numero_usuario <= 99:
    if es_primo(numero_usuario):
        print(f"{numero_usuario} es un número primo.")
    else:
        print(f"{numero_usuario} no es un número primo.")
else:
    print("Por favor, ingrese un número entre 10 y 99.")
