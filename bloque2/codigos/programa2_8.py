#Programa.8  Calificaciones aprobado o desaprobado
#Fecha de elaboración: 24/10/24
#Elaborado por: JOCELYN DE LUNA

num1 = float(input("ingresa tu primer calificación:"))
num2 = float(input("ingresa tu segunda calificación:"))
num3 = float(input("ingresa tu tercera calificación:"))
num4 = float(input("ingresa tu cuarta calificacion:"))
num5 = float(input("ingresa tu quinta calificacion:"))
num6 = float(input("ingresa tu sexta calificacion:"))

calificaciones = (num1+num2+num3+num4+num5+num6)/6

if   calificaciones >=70:
   print("Aprobaste tus materias... !FELICIDADES¡" )



else:
   print("Desaprobaste tus materias... Vuelve a intentarlo !si se puede¡ ")
