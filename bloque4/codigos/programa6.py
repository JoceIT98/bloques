#Programa 4.6 "Programa que utilice una función para realizar operaciónes matematicas basicas"
#Elaborado el 14/11/2024
#Elaborado por : Evelyn Jocelyn León de Luna

def operaciones(num1,num2,digitos):
    suma = num1 + num2
    resta = num1 - num2
    multiplicación = num1 * num2
    division = float(num1/num2)

    modulo = num1 % num2
    print(f'la suma de {num1} + {num2} es: {suma}')
    print(f'la resta de {num1} - {num2} es: {resta}')
    print(f'la multiplicación de {num1} * {num2} es: {multiplicación}')
    print(f'la division de {num1} / {num2} es: {division:{digitos}f}')
    print(f'el modulo de {num1} % {num2} es: {modulo:}\n\n')


#Solicitar datos al usuario
num2 = int(input('Ingrese el segundo número: '))    
num1 = int(input('Ingrese el primer número: '))    
digitos = int(input('''Ingrese la cantidad de decimales a mostrar en la división y modulo:
'''))    

operaciones(num1,num2,digitos)
operaciones(140,8,5)
