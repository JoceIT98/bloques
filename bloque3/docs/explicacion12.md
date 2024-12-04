## Descripción del código: 12
## Definición de la lista mi_lista:

La lista mi_lista contiene cinco colores: ["Rojo", "Verde", "Morado", "Azul", "Naranja"].
```
mi_lista = ["Rojo", "Verde", "Morado", "Azul", "Naranja"]
```
Uso de pop() para eliminar el último elemento:

La línea:
```
ultimo_elemento = mi_lista.pop()
```
utiliza el método pop() sin un índice para eliminar y devolver el
último elemento de la lista. En este caso, el último elemento es "Naranja". El valor eliminado se guarda en la variable ultimo_elemento.
Impresión del elemento eliminado y la lista modificada:

La línea:
```
print("Elemento eliminado:", ultimo_elemento)
```
imprime el elemento eliminado, que es "Naranja".

La línea:
```
print("Lista después de usar pop:", mi_lista)
```
imprime la lista después de eliminar el último elemento. Ahora la lista es ["Rojo", "Verde", "Morado", "Azul"].
Uso de pop() con un índice específico:

La línea:
```
elemento_en_posicion_1 = mi_lista.pop(1)
```
utiliza pop(1) para eliminar y devolver el elemento en la posición 1 de la lista. En este caso, el elemento en la posición 1 es "Verde". El valor eliminado se guarda en la variable elemento_en_posicion_1.
Impresión del elemento eliminado y la lista modificada nuevamente:

La línea:
```
print("Elemento eliminado en la posición 1:", elemento_en_posicion_1)
```
imprime el elemento eliminado en la posición 1, que es "Verde".

La línea:
```
print("Lista después de usar pop en la posición 1:", mi_lista)
```
imprime la lista después de eliminar el elemento en la posición 1. Ahora la lista es ["Rojo", "Morado", "Azul"].
