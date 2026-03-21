"""
Ejercicio 4 — Medio
Crea un programa que gestione las calificaciones de varios estudiantes. 
Usa un diccionario donde cada estudiante tiene una lista de calificaciones.
 Implementa funciones para agregar calificación, obtener promedio de un estudiante y mostrar el ranking de mejores promedios.
Estudiantes:
1. Carlos  → promedio: 9.2
2. Ana     → promedio: 8.7
3. Luis    → promedio: 7.4

Carlos tiene la mejor calificación individual: 10
"""
estudiantes = {
    "Ana": [85, 90, 88],
    "Luis": [70, 75, 80],
    "Sara": [95, 100, 92]
}

def buscar_estudiante(estudiantes, nombre_usuario):
    for nombre in estudiantes:
        if nombre.lower() == nombre_usuario.lower():
            return nombre
    return None


def agregar_calificacion(estudiantes):
    nombre_usuario = input("Nombre de estudiante: ")
    nombre = buscar_estudiante(estudiantes, nombre_usuario)

    if nombre:
        calificacion = int(input("Ingresa calificacion: "))
        estudiantes[nombre].append(calificacion)
        print("Calificación agregada")
    else:
        print("El estudiante no existe")


def promedio_estudiante(estudiantes):
    nombre_usuario = input("Nombre de estudiante: ")
    nombre = buscar_estudiante(estudiantes, nombre_usuario)

    if nombre:
        calificaciones = estudiantes[nombre]
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Promedio de {nombre}: {round(promedio,2)}")
    else:
        print("El estudiante no existe")


def ranking(estudiantes):
    lista_promedios = []

    for nombre, calificaciones in estudiantes.items():
        promedio = sum(calificaciones) / len(calificaciones)
        lista_promedios.append((nombre, promedio))

    lista_ordenada = sorted(lista_promedios, key=lambda x: x[1], reverse=True)

    print("\n--- Ranking ---")
    for i, (nombre, promedio) in enumerate(lista_ordenada, 1):
        print(f"{i}. {nombre} → promedio: {round(promedio,2)}")


def mejor_calificacion(estudiantes):
    mejor = 0
    alumno = ""

    for nombre, calificaciones in estudiantes.items():
        max_cal = max(calificaciones)
        if max_cal > mejor:
            mejor = max_cal
            alumno = nombre

    print(f"\n{alumno} tiene la mejor calificación individual: {mejor}")


# --- Menú ---
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar calificación")
    print("2. Ver promedio de estudiante")
    print("3. Ver ranking")
    print("4. Mejor calificación")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_calificacion(estudiantes)
    elif opcion == "2":
        promedio_estudiante(estudiantes)
    elif opcion == "3":
        ranking(estudiantes)
    elif opcion == "4":
        mejor_calificacion(estudiantes)
    elif opcion == "5":
        print("Adiós")
        break
    else:
        print("Opción inválida")