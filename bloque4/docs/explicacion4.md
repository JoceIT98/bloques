## Código explicado: Programa 4
## La función saludar(nombre) tiene como propósito imprimir un saludo personalizado para la persona cuyo nombre se pase como argumento. A continuación se detalla el comportamiento y uso de la función.

Código:

def saludar(nombre):
Imprime un saludo personalizado con el nombre proporcionado.
```
    print(f'\n¡Hola, {nombre}¡')
```

Imprime una pregunta sobre cómo se encuentra la persona.
``` 
    print(f'¿Cómo estás?')
```

# Expresa un deseo de bienestar para la persona.
```
    print('¡Espero que te encuentres bien!\n')  
```
# Llamadas a la función con diferentes nombres
saludar('Edinguer')
saludar('Chuyito')
saludar('terricola')
Explicación:
Definición de la función saludar(nombre):
La función toma un argumento llamado nombre, que es una cadena de texto (string).
Dentro de la función, se imprimen tres mensajes:
El primero usa un f-string para saludar al nombre proporcionado: ¡Hola, {nombre}¡.
El segundo mensaje pregunta: ¿Cómo estás?.
El tercer mensaje expresa buenos deseos: ¡Espero que te encuentres bien!.
Llamadas a la función:
``````
saludar('Edinguer'): Imprime el saludo personalizado para "Edinguer".
saludar('Chuyito'): Imprime el saludo personalizado para "Chuyito".
saludar('terricola'): Imprime el saludo personalizado para "terricola".
Resultado de las llamadas:
Para saludar('Edinguer'), se imprimirá:


¡Hola, Edinguer¡
¿Cómo estás?
¡Espero que te encuentres bien!
Para saludar('Chuyito'), se imprimirá:


¡Hola, Chuyito¡
¿Cómo estás?
¡Espero que te encuentres bien!
Para saludar('terricola'), se imprimirá:


¡Hola, terricola¡
¿Cómo estás?
¡Espero que te encuentres bien!
```
