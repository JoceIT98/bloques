## Descripción del código: 9
## Definición de las listas:

La lista puntos contiene los valores [10, 30, 20].

La lista puntos_2 es idéntica a puntos, también con los valores [10, 30, 20].

La lista ordenados contiene los valores [10, 20, 30], que
son los mismos números que puntos, pero en un orden diferente.

La lista puntos_texto contiene los valores ["10", "20", "30"], que son
cadenas de texto (en lugar de números enteros como en las otras listas).

Comparaciones:

La línea:

```
print(puntos == puntos_2)

```
compara las listas puntos y puntos_2. Como ambas listas tienen los mismos
elementos en el mismo orden, esta comparación devuelve True.

La línea:
```
print(puntos == ordenados)

```
compara las listas puntos y ordenados. Aunque ambas listas contienen los
mismos números, los elementos están en un orden diferente. En Python, las listas son sensibles al orden de los elementos, por lo que esta comparación devuelve False.

La línea:
```
print(puntos == puntos_texto)
```
compara las listas puntos y puntos_texto. Aunque las listas contienen los mismos 
números, en puntos_texto los valores son cadenas de texto (en lugar de enteros). Por l
o tanto, la comparación devuelve False.

Resumen de resultados:
puntos == puntos_2: True (Las listas son iguales).

puntos == ordenados: False (Las listas tienen los mismos elementos, pero en orden diferente).

puntos == puntos_texto: False (Las listas contienen el mismo conjunto de números, pero en puntos_texto son cadenas de texto, no enteros).
puntos != puntos_2: False (Las listas son iguales, por lo tanto no son diferentes).

puntos != ordenados: True (Las listas son diferentes debido al orden de los elementos).
puntos != puntos_texto: True (Las listas son diferentes porque los elementos son de tipos de datos diferentes: enteros vs. cadenas de texto).
