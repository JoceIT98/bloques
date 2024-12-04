## DescripciÓn del program 2 del bloque 2
El código se compone de varias líneas que demuestran la negación de la operación OR:

Negación de OR con dos valores falsos:
```python
print(not(False or False))  # Si hay fiesta
```
En este caso, la expresión False or False evalúa como False, y la negación
not la convierte en True, lo que significa que "hay fiesta".

 Negación de OR con un valor falso y un valor verdadero:
```python
print(not(False or True))  # No hay fiesta
```
En este caso, la expresión False or True evalúa como True, y la negación not la convierte en False, lo que significa que "no hay fiesta".

 Negación de OR con un valor verdadero y un valor falso:
``` python
print(not(True or False))  # No hay fiesta
```
En este caso, la expresión True or False evalúa como True, y la negación not la convierte en False, lo que significa que "no hay fiesta".

 Negación de OR con dos valores verdaderos:
``` python
print(not(True or True))  # No hay fiesta
```
En este caso, la expresión True or True evalúa como True, y la negación not
la convierte en False, lo que significa que "no hay fiesta".
