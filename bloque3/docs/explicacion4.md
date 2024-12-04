## Descripción del programa 4
## Estructura del código
Definición de la función calcular_impuesto:

La función recibe como entrada el ingreso del empleado.
Según el rango de ingreso, aplica un porcentaje distinto para calcular el impuesto:
Un bloque else que parece no tener propósito, ya que los casos anteriores abarcan todos los ingresos posibles.

Cálculo de impuestos y salario final:
```
ingreso_empleado = float(input("¿Cuales son tus ingresos?: "))
impuesto_a_pagar = calcular_impuesto(ingreso_empleado)
salario_final = ingreso_empleado - impuesto_a_pagar
```
El programa solicita al usuario sus ingresos y los convierte a tipo float.
Llama a calcular_impuesto para determinar cuánto debe pagar de impuestos.
Resta el impuesto al ingreso para obtener el salario final.

Muestra los resultados:
```
print(f"Tus impuestos son: ${impuesto_a_pagar:.2f}")
print(f"Tu salario final es: ${salario_final:.2f}")
Imprime el monto de impuestos y el salario final con dos decimales para mayor claridad.
```
Imprime el monto de impuestos y el salario final con dos decimales para mayor claridad.
