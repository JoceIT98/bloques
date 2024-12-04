## Código explicado: Programa 8


Explicación del Código:
Función operaciones(num1, num2, digitos):

Esta función realiza las operaciones matemáticas básicas: suma, resta, multiplicación, división y módulo entre num1 y num2, y presenta los resultados de manera formateada.


# Parámetros:
num1: Primer número (entero).


num2: Segundo número (entero).


digitos: Número de decimales a mostrar en la división y el módulo.


El formato de la división se ajusta según el número de decimales especificados por el usuario mediante f-string (e.g., division:{digitos}f).
Ciclo while:

El ciclo while permite que el programa se ejecute repetidamente hasta que el usuario decida salir.
Flujo:


En cada ciclo, se solicitan al usuario los valores para num1, num2, el número de decimales (digitos), y el número de iteraciones.


La función operaciones se ejecuta para el número de iteraciones especificado por el usuario. Durante cada iteración, los valores de num1 y num2 se duplican (num1 *= 2 y num2 *= 2).


Después de completar las iteraciones, el programa pregunta al usuario si desea realizar otra operación o salir:


Si el usuario ingresa "salir", el ciclo while se termina y el programa imprime un mensaje de despedida.


Si el usuario presiona "enter" (sin escribir nada), el ciclo while se repite.


# Ejemplo de Ejecución:
Si el usuario ingresa:
```
Primer número: 2
Segundo número: 4
Decimales: 2
Número de iteraciones: 3

```
La salida será algo como:

```
Ingrese el segundo número: 4
Ingrese el primer número: 2
Ingrese la cantidad de decimales a mostrar en la división y módulo: 2
Ingrese el número de iteraciones: 3

La suma de 2 + 4 es: 6
La resta de 2 - 4 es: -2
La multiplicación de 2 * 4 es: 8
La división de 2 / 4 es: 0.50
El módulo de 2 % 4 es: 2


La suma de 4 + 8 es: 12
La resta de 4 - 8 es: -4
La multiplicación de 4 * 8 es: 32
La división de 4 / 8 es: 0.50
El módulo de 4 % 8 es: 4


La suma de 8 + 16 es: 24
La resta de 8 - 16 es: -8
La multiplicación de 8 * 16 es: 128
La división de 8 / 16 es: 0.50
El módulo de 8 % 16 es: 8

¿Desea realizar otra operación? (Escriba 'salir' para terminar o enter para continuar):
```
