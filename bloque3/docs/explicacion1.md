## Código explicado: Programa 1
## Definición del tipo de mascota:

```
mascota = input("Ingresa el tipo de mascota: ")
```
Aquí el programa solicita al usuario ingresar un texto que describe su mascota. El texto que ingrese será almacenado en la variable mascota.

Estructura condicional:
```
if "perro" in mascota:
    print("Es un perro")
```
Se evalúa si la palabra "perro" está contenida dentro del texto ingresado.
Si lo está, se imprime "Es un perro".
```
elif "gato" in mascota:
    print("Tienes un gato")
```
Si "perro" no está en el texto, se verifica si la palabra "gato" está presente.
Si es así, se imprime "Tienes un gato".

