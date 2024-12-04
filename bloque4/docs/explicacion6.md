## Código explicado: Programa 6
La función operaciones(num1, num2, digitos) realiza cinco operaciones matemáticas básicas entre dos números y presenta los resultados de una manera formateada. A continuación se explica el comportamiento y la lógica de la función.

Código:
```
def operaciones(num1, num2, digitos):
    suma = num1 + num2
    resta = num1 - num2
    multiplicación = num1 * num2
    division = float(num1 / num2)  # Se asegura que la división sea un número flotante.
    modulo = num1 % num2
    
    print(f'La suma de {num1} + {num2} es: {suma}')
    print(f'La resta de {num1} - {num2} es: {resta}')
    print(f'La multiplicación de {num1} * {num2} es: {multiplicación}')
    print(f'La división de {num1} / {num2} es: {division:{digitos}f}')  # Formatea la división con los decimales especificados.
    print(f'El módulo de {num1} % {num2} es: {modulo}\n\n')
```
# Solicitar datos al usuario
```
num2 = int(input('Ingrese el segundo número: '))    
num1 = int(input('Ingrese el primer número: '))    
digitos = int(input('''Ingrese la cantidad de decimales a mostrar en la división y modulo:\n'''))    

operaciones(num1, num2, digitos)  # Llamada a la función con los datos ingresados por el usuario
operaciones(140, 8, 5)  # Llamada a la función con valores predeterminados
```

# Explicación:
```
Definición de la función operaciones(num1, num2, digitos):
Parámetros:
num1: Primer número (entero).
num2: Segundo número (entero).

digitos: Número de decimales a mostrar en la división y el módulo (entero).


La función realiza las siguientes operaciones matemáticas:
```
Suma: num1 + num2
Resta: num1 - num2
Multiplicación: num1 * num2
División: num1 / num2 (asegurando que el resultado sea un número flotante usando float()).
Módulo: num1 % num2 (el residuo de la división).
```

Luego, se imprimen los resultados de estas operaciones, con un formato adecuado:
Se utiliza el formato f'{valor:{digitos}f}' para controlar el número de decimales en la división y el módulo.


Entrada de datos por parte del usuario:


Se solicita al usuario que ingrese dos números enteros (num1 y num2), así como el número de decimales que desea mostrar en la división y el módulo.


Llamada a la función:
```
operaciones(num1, num2, digitos): Llama a la función con los valores ingresados por el usuario.
operaciones(140, 8, 5): Llama a la función con valores predeterminados para demostrar cómo funciona la función con datos fijos.
```
Ejemplo de salida:
Si el usuario ingresa:

```
Primer número: 25
Segundo número: 7
Decimales: 2
La salida será algo como:


La suma de 25 + 7 es: 32
La resta de 25 - 7 es: 18
La multiplicación de 25 * 7 es: 175
La división de 25 / 7 es: 3.57
El módulo de 25 % 7 es: 4


La suma de 140 + 8 es: 148
La resta de 140 - 8 es: 132
La multiplicación de 140 * 8 es: 1120
La división de 140 / 8 es: 17.50000
El módulo de 140 % 8 es: 4
```
