#Programa 4.9 Deducir si un numero es primo entre el 10 y 99
#Elaborado el 15/11/2024
#Elaborado por : Evelyn Jocelyn León de Luna

import math 
numero = int(input("Ingrese un número entre 10 y 99: "))


if 10 <= numero <= 99:
    es_primo = True #una variable que determine si es primo 
    

    for i in range(2, int(math.sqrt(numero)) + 1):  
        if numero % i == 0:
            es_primo = False  # Si es divisible, no es primo
            break 
    
#Resultado
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
else:
    print("Por favor, ingrese un número entre 10 y 99.")
