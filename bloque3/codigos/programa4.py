# Programa 4 Impuestos de un empleado
# Fecha: 2024/10/29
# Elaborado por: Evelyn Jocelyn León de Luna
def calcular_impuesto(ingreso):
    if ingreso <= 1000:
        impuesto = ingreso * 0.05
    elif ingreso >1000 and ingreso <= 2500:
        impuesto = ingreso * 0.08 
    elif ingreso >2500 and ingreso < 6000:
        impuesto = ingreso * 0.12
    elif ingreso >= 6000:
        impuesto = ingreso * 0.15
    else:
        impuesto = (1000 * 0.05) + (2500 * 0.08) + (2501 * 0.12) + (6000 * 0.15)
    
    return impuesto

# Solicitar el ingreso al usuario
ingreso_empleado = float(input("¿Cuales son tus ingresos?: "))
impuesto_a_pagar = calcular_impuesto(ingreso_empleado)

# Calcular el salario final
salario_final = ingreso_empleado - impuesto_a_pagar

# Mostrar resultados
print(f"Tus impuestos son: ${impuesto_a_pagar:.2f}")
print(f"Tu salario final es: ${salario_final:.2f}")
