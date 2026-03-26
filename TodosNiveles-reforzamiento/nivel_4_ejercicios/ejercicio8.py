# ------------------------------------------------------------
# EJERCICIO 8 — Desafío
# Procesa un archivo de texto simulado (string multilínea)
# con datos de empleados y genera reportes.
# Formato de cada línea: "nombre,departamento,salario"
# ------------------------------------------------------------
datos_empleados = """Ana,Sistemas,25000
Luis,Ventas,18000
María,Sistemas,28000
Carlos,RRHH,20000
Pedro,Ventas,22000
Laura,Sistemas,30000
Jorge,RRHH,19000
Sofia,Ventas,21000"""

# Output esperado:
# Total empleados: 8
#
# Por departamento:
#   Sistemas: 3 empleados | Salario promedio: $27666.67
#   Ventas:   3 empleados | Salario promedio: $20333.33
#   RRHH:     2 empleados | Salario promedio: $19500.00
#
# Empleado mejor pagado:  Laura (Sistemas) - $30000
# Empleado menor salario: Luis (Ventas)    - $18000
# Masa salarial total:    $183000
