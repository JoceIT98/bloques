# Programa 5 Nivel de desempeño de un estudiante 
# Fecha: 2024/10/29
# Elaborado por: Evelyn Jocelyn León de Luna
# Solicitar la calificación al usuario
calificación = float(input("Calificación del estudiante (0-100): "))

# Determinar el nivel de desempeño
if calificacion <= 60:
    desempeño = "Insuficiente"
elif 60 < calificación <= 79 :
    desempeño = "Suficiente"
elif 79 < calificación <= 89:
    desempeño = "Muy bien"
elif 89 < calificación <= 95:
    desempeño = "Notable"
elif 95 < calificación <= 100:
    desempeño = "Excelente"

# Mostrar el resultado
print(f"El nivel de desempeño es: {desempeno}")
