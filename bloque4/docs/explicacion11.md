Función es_primo(numero):

La función recibe un número y verifica si es primo.
Condición Inicial: Si el número es menor que 2, se retorna False porque los números menores a 2 no son primos.
Cálculo de Primalidad: La función recorre los números desde 2 hasta la raíz cuadrada de numero (sqrt(numero)). Si el número es divisible por algún valor dentro de este rango, retorna False. Si no es divisible por ninguno de estos valores, retorna True, indicando que el número es primo.
Entrada del Usuario y Bucle while:

El programa usa un bucle while para permitir múltiples entradas del usuario.
Se le pide al usuario que ingrese un número entre 10 y 99 o la palabra "salir" para terminar el programa.
Si el usuario ingresa "salir", el programa imprime un mensaje de despedida y termina el bucle con break.
Manejo de Errores:

Si la entrada no es un número válido (por ejemplo, si el usuario ingresa texto o caracteres no numéricos), se maneja mediante un bloque try-except que captura la excepción ValueError. Si esto ocurre, el programa solicita una nueva entrada con un mensaje de error.
Si la entrada es un número, el programa verifica si está en el rango de 10 a 99. Si está dentro de este rango, se comprueba si es primo mediante la función es_primo(). Si el número es primo, se imprime el resultado; si no lo es, se indica que no es primo.
Ejemplo de Ejecución:
Caso 1: El número es primo:

Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: 29
29 es un número primo.
Caso 2: El número no es primo:

Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: 30
30 no es un número primo.
Caso 3: Entrada fuera de rango:

Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: 5
Por favor, ingrese un número entre 10 y 99.
Caso 4: Entrada no válida:

Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: abc
Por favor, ingrese un número válido o 'salir' para terminar.
Caso 5: Salir del programa:

Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: salir
¡Hasta luego, gracias por usar mi programa!

