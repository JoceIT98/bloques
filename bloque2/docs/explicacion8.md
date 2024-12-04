## Descripcion del programa 8 del bloque 2
Estructura del código

El código se compone de varias secciones:

Solicitud de calificaciones:
 El programa solicita al usuario que ingrese las calificaciones de las 5 unidades.
``` python
u1 = int(input("Calificacion de la unidad 1: "))
u2 = int(input("Calificacion de la unidad 2: "))
u3 = int(input("Calificacion de la unidad 3: "))
u4 = int(input("Calificacion de la unidad 4: "))
u5 = int(input("Calificacion de la unidad 5: "))
```

Cálculo del promedio: El programa calcula el promedio de las 5 unidades sumando
 las calificaciones y dividiendo por 5.
```python
promedio = (u1 + u2 + u3 + u4 + u5) / 5
```

 Evaluación del promedio: El programa evalúa si el promedio es mayor o igual a 7.
 Si es así, el estudiante aprobó; de lo contrario, reprobó.
``` python
if promedio >= 7:
    print("Usted aprobo")
else:
    print("Usted reprobo")
```


- El código utiliza la función input() para obtener entrada del usuario.
- Las variables u1, u2, u3, u4 y u5 se utilizan para almacenar las calificaciones de las 5 unidades.
- El código utiliza una condición if-else para evaluar si el estudiante aprobó o reprobó.
- El código imprime el resultado utilizando la función print().
