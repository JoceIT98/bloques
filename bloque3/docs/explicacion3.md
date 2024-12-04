## Descripcón del programa 3
## Explicación del código
Entrada del usuario como cadena:

```
variable = input("Ingresa tu edad: ")
print(type(variable))
```

Se utiliza input() para solicitar la edad al usuario. Esta función siempre retorna un dato de tipo cadena (str), sin importar lo que el usuario ingrese.
Se utiliza type(variable) para imprimir el tipo de dato, que será <class 'str'>.

Conversión a entero:
```
variable = int(variable)  # Convertir la variable a tipo entero 
print(type(variable))
```
La función int() convierte la cadena ingresada en un número entero.
Si el usuario ingresa algo que no puede ser convertido (por ejemplo, texto no numérico), el programa generará un error.
type(variable) ahora imprimirá <class 'int'>.

Conversión a flotante:
```
variable = float(variable)  # Convertir la variable a tipo flotante
print(type(variable))
```
La función float() convierte el número entero almacenado en la variable a un número flotante (con decimales).
type(variable) imprimirá <class 'float'>.
