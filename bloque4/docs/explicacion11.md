## Código explicado: Programa 11



Función es_primo(numero):

La función recibe un número y verifica si es primo.


Condición Inicial: Si el número es menor que 2, se retorna False porque los números menores a 2 no son primos.

```
import math
def es_primo(numero):
    if numero < 2:
        return False   
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False   
    return True  

```

Cálculo de Primalidad: La función recorre los números desde 2 hasta la raíz cuadrada de numero (sqrt(numero)). Si el número es divisible por algún
valor dentro de este rango, retorna False. Si no es divisible por ninguno de estos valores, retorna True, indicando que el número es primo.
Entrada del Usuario y Bucle while:


El programa usa un bucle while para permitir múltiples entradas del usuario.


Se le pide al usuario que ingrese un número entre 10 y 99 o la palabra "salir" para terminar el programa.


Si el usuario ingresa "salir", el programa imprime un mensaje de despedida y termina el bucle con break.
Manejo de Errores:

```
while True:
    entrada = input("Ingrese un número entre 10 y 99 para verificar si es primo o 'salir' para terminar: ").lower()  
    if entrada == "salir":
        print("¡Hasta luego, gracias por usar mi programa!")
        break
```

Si la entrada no es un número válido (por ejemplo, si el usuario ingresa texto o caracteres no numéricos), se maneja mediante un bloque try-except que captura la excepción ValueError. Si esto ocurre, el programa solicita una nueva entrada con un mensaje de error.


Si la entrada es un número, el programa verifica si está en el rango de 10 a 99. Si está dentro de este rango, se comprueba si es primo mediante la función es_primo(). Si el número es primo, se imprime el resultado; si no lo es, se indica que no es primo.

```
       else:
                print(f"{numero_usuario} no es un número primo.")
        else:
            print("Por favor, ingrese un número entre 10 y 99.")
    except ValueError:
        print("Por favor, ingrese un número válido o 'salir' para terminar.")

```
# Fin

