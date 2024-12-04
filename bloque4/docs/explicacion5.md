## Código explicado: Programa 5
# La función saludar(nombre, edad) saluda de manera personalizada e incluye la edad de la persona. A continuación, se explica su comportamiento y uso.

Código:
```
def saludar(nombre, edad):
    print(f'\n¡Hola, {nombre}¡')          # Imprime un saludo personalizado con el nombre.
    print(f'Tienes {edad} años.')         # Imprime la edad de la persona.
    print('¡Espero que te encuentres bien!\n')  # Expresa un deseo de bienestar para la persona.
``````

# Llamadas a la función con diferentes nombres y edades
saludar('Edinguer', edad=26)
saludar('Chuyito', edad=18)
saludar('terricola', edad=23)
Explicación:
Definición de la función saludar(nombre, edad):

La función recibe dos parámetros:
nombre: Un string que representa el nombre de la persona.
edad: Un número (entero o flotante) que representa la edad de la persona.
< br >Dentro de la función, se imprimen tres mensajes:    < br / >
< br >El primer mensaje utiliza un f-string para saludar a la persona con su nombre: ¡Hola, {nombre}¡.< br / >
< br >El segundo mensaje imprime la edad de la persona: Tienes {edad} años..< br / >
< br >El tercer mensaje expresa un deseo de bienestar: ¡Espero que te encuentres bien!.< br / >
Llamadas a la función:
``````
saludar('Edinguer', edad=26): Imprime un saludo personalizado con el nombre "Edinguer" y la edad "26".
saludar('Chuyito', edad=18): Imprime un saludo personalizado con el nombre "Chuyito" y la edad "18".
saludar('terricola', edad=23): Imprime un saludo personalizado con el nombre "terricola" y la edad "23".
Resultado de las llamadas:
Para saludar('Edinguer', edad=26):
```

¡Hola, Edinguer¡
Tienes 26 años.
¡Espero que te encuentres bien!
Para saludar('Chuyito', edad=18):


¡Hola, Chuyito¡
Tienes 18 años.
¡Espero que te encuentres bien!
Para saludar('terricola', edad=23):


¡Hola, terricola¡
Tienes 23 años.
¡Espero que te encuentres bien!
