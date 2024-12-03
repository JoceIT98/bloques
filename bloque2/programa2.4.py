#Programa.2.4  Programa que calcula los impuestos y dar un valor
#Fecha de elaboración: 22/10/24
#Elaborado por: JOCELYN DE LUNA

def calcular_impuesto(valor, tasa_impuesto):
  impuesto = valor * (tasa_impuesto / 100)
  return impuesto

valor = float (input("Introduce el valor:"))
tasa_impuesto = float(input("introduce la tasa de impuesto en %:"))

print(f"El impuesto sobre {valor} con una tasa del {tasa_impuesto}% es: {calcular_impuesto(valor, tasa_impuesto):.2f}""\nGracias por usar nuestro sistema!")
