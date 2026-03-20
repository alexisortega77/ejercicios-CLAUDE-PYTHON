"""
Ejercicio 6 — Medio
Dado una lista de calificaciones, usa list comprehension para crear tres listas nuevas: aprobados (≥60), reprobados (<60) y l
as calificaciones elevadas al cuadrado.
Calificaciones: [45, 78, 92, 55, 88, 61, 30, 75]
Aprobados:  [78, 92, 88, 61, 75]
Reprobados: [45, 55, 30]
Cuadrados:  [2025, 6084, 8464, 3025, 7744, 3721, 900, 5625]
"""
calificaciones=[45, 78, 92, 55, 88, 61, 30, 75]
aprobados=[i  for i in  calificaciones if i>=60]
reprobados=[i  for i in  calificaciones if i<60]
cuadrados=[i**2  for i in  calificaciones]

print("Calificaciones: ", calificaciones)
print("Aprobados: ",aprobados)
print("Reprobado: ",reprobados)
print("Cuadrados: ",cuadrados)

#SOLUCION OPTIMA
def analizar_calificaciones(calificaciones):
    aprobados  = [c for c in calificaciones if c >= 60]
    reprobados = [c for c in calificaciones if c < 60]
    cuadrados  = [c ** 2 for c in calificaciones]

    print(f"Calificaciones: {calificaciones}")
    print(f"Aprobados:      {aprobados}  ({len(aprobados)} alumnos)")
    print(f"Reprobados:     {reprobados}  ({len(reprobados)} alumnos)")
    print(f"Cuadrados:      {cuadrados}")
    print(f"Promedio:       {sum(calificaciones) / len(calificaciones):.2f}")

analizar_calificaciones([45, 78, 92, 55, 88, 61, 30, 75])