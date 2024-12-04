## Código explicado: Programa 2
## Primer bloque:

nombres = ["luis", "Juan", "Eduardo", "Marcos", "Chuy"]

Este código recorre la lista nombres e imprime cada uno de sus elementos, precedido de la cadena "El nombre es ".
```
for nombre in nombres:
    print("El nombre es ", nombre)
```
Segundo bloque (Repetir sin print individual):
Si deseas imprimir los nombres sin escribir un print para cada uno, puedes usar un ciclo for junto con la función join para unir los elementos en una cadena, o simplemente contar los elementos y hacer algo con la cantidad.

Ejemplo con el número de elementos:

```
print("Hay", len(nombres), "nombres en la lista.")
Esto muestra cuántos nombres hay en la lista, sin necesidad de imprimirlos uno por uno.
```

Tercer bloque (Repetir acción con otra lista):
```
frutas = ["Manzana", "Piña", "Platano"]

for fruta in frutas:
    print("La fruta es:", fruta)
```
Este ciclo recorre la lista frutas y imprime "La fruta es:" seguido del nombre de cada fruta. Es un ejemplo similar al primer bloque, pero con una lista distinta.
