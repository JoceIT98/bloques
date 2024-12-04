## Descripción del programa 6 del bloque1
 El programa está diseñado para calcular el área de un triángulo utilizando la fórmula matemática básica:

Solicitar datos al usuario.
```Python 
 base = float(input("Introduce la base del triangulo: "))
 altura = float(input("Introduce la altura del triangulo: "))
```
input: Se utiliza para pedir al usuario que ingrese valores.
float: Convierte el valor ingresado (que inicialmente es texto) en un número decimal.
Esto permite realizar operaciones matemáticas más precisas.
``` Python
print(f"El area del triangulo es: " + str(area))
```
Se utiliza la función print para mostrar el resultado al usuario.
f-string: Permite incluir valores en un texto de forma dinámica.
str: Convierte el valor numérico del área a texto para que pueda combinarse con el mensaje.
