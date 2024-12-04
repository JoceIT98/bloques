## Descripción del programa 9 del bloque 2 
El código se compone de varias secciones:

Solicitud de cantidad de artículos:
 El programa solicita al usuario que ingrese la cantidad de artículos que desea comprar.
``` python
articulos = int(input("Cantidad de articulos: "))
```

 Condición de precio:
El programa evalúa si la cantidad de artículos es mayor a 3. Si es mayor a 3,
el precio unitario es de $30; de lo contrario, el precio unitario es de $45.
```pyhton
if articulos > 3:
    total = articulos * 30
else:
    total = articulos * 45
```

- El código utiliza la función input() para obtener entrada del usuario.
- La variable articulos se utiliza para almacenar la entrada del usuario.
- El código utiliza una condición if-else para evaluar el precio unitario según la cantidad de artículos.
- El código imprime el resultado utilizando la función print() y convirtiendo el total a una cadena de texto utilizando la función str().
