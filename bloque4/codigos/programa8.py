#Programa 4.8 Agregar a p-7 un While para que se repita el programa hasta que se ingrese salir con la funcion .lower
#Elaborado el 14/11/2024
#Elaborado por : Evelyn Jocelyn León de Luna

def operaciones(num1, num2, digitos): 
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = float(num1 / num2)
    modulo = num1 % num2
    print(f'La suma de {num1} + {num2} es: {suma}')
    print(f'La resta de {num1} - {num2} es: {resta}')
    print(f'La multiplicación de {num1} * {num2} es: {multiplicacion}')
    print(f'La división de {num1} / {num2} es: {division:{digitos}f}')
    print(f'El módulo de {num1} % {num2} es: {modulo}\n\n')


# Ciclo while, repetir el programa hasta que el usuario ingrese "salir"
while True:
    # Solicitar datos al usuario
    num2 = int(input('Ingrese el segundo número: '))
    num1 = int(input('Ingrese el primer número: '))
    digitos = int(input('Ingrese la cantidad de decimales a mostrar en la división y módulo: '))
    iteraciones = int(input('Ingrese el número de iteraciones: '))

    # Ejecutar la operación para cada iteración, duplicando los valores en cada ciclo
    for i in range(iteraciones):
        operaciones(num1, num2, digitos)
        # Duplicar los valores de num1 y num2 para la siguiente iteración
        num1 *= 2
        num2 *= 2

    # Preguntar al usuario si desea continuar o salir
    respuesta = input("¿Desea realizar otra operación? (Escriba 'salir' para terminar o enter para continuar): ").lower()
    if respuesta == "salir":
        print("¡Hasta luego!")
        break  # Salir del ciclo
