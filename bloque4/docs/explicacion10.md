## Código explicado: Programa 10


Explicación del Código:
Función es_primo(numero):

Esta función determina si un número es primo o no.

Condición Inicial: Si el número es menor que 2, retorna False, ya que los números menores a 2 no son considerados primos.


Verificación de Divisibilidad: Utiliza un ciclo for que recorre los números desde 2 hasta la raíz cuadrada del número (sqrt(numero)). Si el número 
es divisible por alguno de estos valores, se considera que no es primo y se retorna False. Si no se encuentra ningún divisor, el número es primo y la función retorna True.

```
def es_primo(numero):
    if numero < 2:
        return False
    
    # divisible entre 2 y raiz
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False  #Divisible, no es primo
    
    return True 

```
Entrada del Usuario:

Se solicita al usuario ingresar un número entero entre 10 y 99. El número ingresado se almacena en la variable numero_usuario.


Verificación y Resultado:



Se verifica si el número ingresado está dentro del rango de 10 a 99. Si está fuera de este rango, se muestra un mensaje pidiendo que ingrese un número válido.


Si el número está en el rango, se llama a la función es_primo(numero_usuario) para verificar su primalidad. Dependiendo del resultado, se imprime si el número es primo o no.
