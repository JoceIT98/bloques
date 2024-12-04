## Descripción del Programa 2
## Código explicado
Lectura de los números:

```
n1 = int(input("ingresa el numero 1: "))
n2 = int(input("ingresa el numero 2: "))
```
Se solicita al usuario ingresar dos números enteros.
Las entradas se convierten en tipo int para poder realizar comparaciones numéricas.
Estructura condicional para comparar los números:

Primer caso:
```
if n1 > n2:
    print ("El numero " + str(n1) + " es mayor al " + str(n2))
```

Si el primer número es mayor que el segundo, se imprime un mensaje indicando que es mayor.
Se convierte el número a str para concatenar con el mensaje.
```
elif n1 == n2:
    print("Son números iguales")
```

Si ambos números son iguales, se imprime el mensaje correspondiente.
```
else:
    print("El numero " + str(n1) + " es menor al número " + str(n2))
```
Si no se cumple ninguna de las condiciones anteriores, el programa concluye que el primer número es menor.

