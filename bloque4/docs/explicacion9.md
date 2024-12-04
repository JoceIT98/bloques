## Código explicado: Programa 9




# Entrada del Usuario:

El programa solicita al usuario ingresar un número entre 10 y 99. Este número se almacena en la variable numero.


Condición de Rango:

Se verifica si el número ingresado está dentro del rango de 10 a 99 (if 10 <= numero <= 99). Si no es así, el programa pide que ingrese un número dentro de este rango.


Inicialización de la Variable es_primo:

Se establece es_primo = True como una suposición inicial, ya que consideramos que el número puede ser primo.



Cálculo de la Primalidad:

El programa verifica si el número es divisible por algún número entre 2 y la raíz cuadrada de numero (inclusive). Esto se debe a que si un número no tiene factores primos menores que su raíz cuadrada, no los tendrá mayores. Esto hace que la verificación sea más eficiente.
```

Ciclo for: Se recorre desde 2 hasta sqrt(numero) + 1. Si el número es divisible por cualquiera de estos valores (es decir, numero % i == 0), se establece es_primo = False y se termina el ciclo con break, ya que no es necesario seguir buscando más divisores.
Resultado Final:

Si la variable es_primo sigue siendo True después del ciclo, se imprime que el número es primo. Si se encontró un divisor, se imprime que el número no es primo.
Excepciones:

Si el número ingresado no está en el rango de 10 a 99, el programa indica al usuario que ingrese un número válido.
```
