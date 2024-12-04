#Programa 4.11 agregue a p-10 un ciclo while para que se repita el programa
#hasta que se ingrese la palabra salir usando la funcion .lower
#Elaborado el 15/11/2024
#Elaborado por : Evelyn Jocelyn León de Luna

import math
def es_primo(numero):
    if numero < 2:
        return False   
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False   
    return True  

while True:
    entrada = input("Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: ").lower()  
    if entrada == "salir":
        print("¡Hasta luego, gracias por usar mi programa!")
        break
       # Intentar convertir la entrada a un número

    try:
        numero_usuario = int(entrada)
        if 10 <= numero_usuario <= 99:
            if es_primo(numero_usuario):
                print(f"{numero_usuario} es un número primo.")
            else:
                print(f"{numero_usuario} no es un número primo.")
        else:
            print("Por favor, ingrese un número entre 10 y 99.")
    
    # Si la entrada no es un número válido, mostrar un mensaje de error
    except ValueError:
        print("Por favor, ingrese un número válido o 'salir' para terminar.")
