
# ------------------------------------------------------------
# EJERCICIO 5 — Medio
# Crea un sistema de calificaciones con estas funciones:
# - letra(promedio)  → A/B/C/D/F
# - esta_aprobado(promedio) → True/False (mínimo 60)
# - estadisticas(calificaciones) → dict con promedio, mayor, menor, letra
# - reporte(nombre, calificaciones) → imprime todo
# ------------------------------------------------------------
# Output esperado:
# reporte("Carlos", [85, 92, 78, 90, 88])
#
# Estudiante:     Carlos
# Calificaciones: 85, 92, 78, 90, 88
# Promedio:       86.60
# Mayor:          92
# Menor:          78
# Letra:          B
# Estado:         Aprobado
def letter(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def is_approved(average):
    return average >= 60

def statistics(grades):
    average = sum(grades) / len(grades)
    return {
        "average": average,
        "max":     max(grades),
        "min":     min(grades),
        "letter":  letter(average)
    }

def report(name, grades):
    data = statistics(grades)
    status = "Aprobado" if is_approved(data["average"]) else "Reprobado"

    print(f"Estudiante:     {name}")
    print(f"Calificaciones: {', '.join(str(n) for n in grades)}")
    print(f"Promedio:       {data['average']:.2f}")
    print(f"Mayor:          {data['max']}")
    print(f"Menor:          {data['min']}")
    print(f"Letra:          {data['letter']}")
    print(f"Estado:         {status}")

report("Carlos", [85, 92, 78, 90, 88])

print(statistics([85, 92, 78, 90, 88]))
report("alexis", [85, 92, 78, 90, 88])