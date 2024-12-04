## Código explicado: Programa 7
## Definición de la función operaciones(num1, num2, digitos):

Parámetros:
```
num1: Primer número (entero).
num2: Segundo número (entero).
digitos: Número de decimales a mostrar en la división y el módulo (entero).
```

La función realiza las siguientes operaciones entre num1 y num2:
```
Suma: num1 + num2
Resta: num1 - num2
Multiplicación: num1 * num2
División: num1 / num2 (asegurando que el resultado sea un número flotante con float()).
Módulo: num1 % num2 (el residuo de la división).
```

Luego, imprime los resultados de estas operaciones, usando f-strings para el formato. En particular, la división se formatea con el número de decimales especificados por el parámetro digitos.

# Solicitar datos al usuario:
```
num1 y num2: Los números sobre los cuales se realizarán las operaciones.
digitos: Cantidad de decimales que se desea mostrar en los resultados de la división y el módulo.
iteraciones: El número de veces que se ejecutará la función, duplicando los valores de num1 y num2 en cada ciclo.
```
# Ciclo for para iteraciones:
Se ejecuta un bucle for basado en el número de iteraciones ingresado por el usuario. En cada iteración:


Se llama a la función operaciones(num1, num2, digitos) con los valores actuales de num1, num2 y digitos.


Después de cada llamada a la función, los valores de num1 y num2 se duplican (num1 *= 2 y num2 *= 2) para la siguiente iteración.
