# ------------------------------------------------------------
# EJERCICIO 7 — Desafío
# Crea un sistema de estudiantes con:
# - agregar_estudiante(bd, nombre, calificaciones)
# - promedio_estudiante(bd, nombre)
# - ranking(bd) → lista ordenada de mejor a peor promedio
# - reprobados(bd) → estudiantes con promedio < 60
# - estadisticas_grupo(bd) → promedio del grupo, mejor, peor
# ------------------------------------------------------------
# Output esperado:
# bd = {}
# agregar_estudiante(bd, "Ana",    [90, 85, 92, 88])
# agregar_estudiante(bd, "Luis",   [55, 62, 48, 70])
# agregar_estudiante(bd, "María",  [78, 82, 75, 80])
# agregar_estudiante(bd, "Carlos", [95, 98, 92, 97])
#
# promedio_estudiante(bd, "Ana") → 88.75
#
# ranking(bd):
# 1. Carlos → 95.50
# 2. Ana    → 88.75
# 3. María  → 78.75
# 4. Luis   → 58.75
#
# reprobados(bd): ['Luis']
#
# estadisticas_grupo(bd):
# Promedio del grupo: 80.44
# Mejor estudiante:   Carlos (95.50)
# Peor estudiante:    Luis (58.75)
bd={}
def add_student(bd, name, calif):
    bd[name]=calif

    
def student_average(bd, name):
    if name in bd:
        return sum(bd[name])/len(bd[name])
    return None
def ranking(bd):
    return sorted([(name, student_average(bd, name))for name in bd], key=lambda x:x[1], reverse=True)
    
def failed_students(bd):
    return [name for name in bd if student_average(bd, name) <60]

def statitistic_group(bd):
    average = {name: student_average(bd, name) for name in bd}
    group_average=sum(average.values())/len(average)
    the_best=max(average, key=average.get)
    the_worst=min(average, key=average.get)
    return group_average, the_best, the_worst

add_student(bd, "Ana",    [90, 85, 92, 88])
add_student(bd, "Luis",   [55, 62, 48, 70])
add_student(bd, "María",  [78, 82, 75, 80])
add_student(bd, "Carlos", [95, 98, 92, 97])

print(f"Promedio ana: {student_average(bd, "Ana")}")

print("Ranking (bd)")
for i, (name, avg) in enumerate(ranking(bd),1):
    print(f"{i}. {name:<8} -> {avg:.2f}")

print(f"Reprobados (bd): {failed_students(bd)}")

prom_grupo, mejor, peor = statitistic_group(bd)

print("estadisticas_grupo(bd):")
print(f"Promedio del grupo: {prom_grupo:.2f}")
print(f"Mejor estudiante:   {mejor} ({student_average(bd, mejor):.2f})")
print(f"Peor estudiante:    {peor} ({student_average(bd, peor):.2f})")