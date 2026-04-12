biblioteca = {}

def mostrar_disponible(valor):
    return "Sí" if valor else "No"

def agregar_libro(biblioteca):
    nombre = input("Título: ").lower().strip()

    if nombre in biblioteca:
        print(f"'{nombre}' ya existe en la biblioteca.")
        return

    autor = input("Autor: ").lower().strip()
    biblioteca[nombre] = {"autor": autor, "disponible": True}
    print("Libro agregado.")

def prestar_libro(biblioteca):
    nombre = input("Título: ").lower().strip()
    libro  = biblioteca.get(nombre)

    if not libro:
        print(f"'{nombre}' no encontrado.")
        return

    if libro["disponible"]:
        libro["disponible"] = False
        print(f"'{nombre}' prestado exitosamente.")
    else:
        print(f"'{nombre}' ya está prestado.")

def devolver_libro(biblioteca):
    nombre = input("Título: ").lower().strip()
    libro  = biblioteca.get(nombre)

    if not libro:
        print(f"'{nombre}' no existe.")
        return

    if not libro["disponible"]:
        libro["disponible"] = True
        print(f"'{nombre}' devuelto exitosamente.")
    else:
        print(f"'{nombre}' no estaba prestado.")

def buscar_por_autor(biblioteca):
    autor     = input("Autor: ").lower().strip()
    resultado = [(n, d) for n, d in biblioteca.items() if d["autor"] == autor]

    if resultado:
        for nombre, datos in resultado:
            print(f"{nombre} | Disponible: {mostrar_disponible(datos['disponible'])}")
    else:
        print("No se encontraron libros de ese autor.")

def libros_disponibles(biblioteca):
    disponibles = [(n, d) for n, d in biblioteca.items() if d["disponible"]]

    if disponibles:
        print("Libros disponibles:")
        for nombre, datos in disponibles:
            print(f"  {nombre} | Autor: {datos['autor']}")
    else:
        print("Ningún libro disponible en este momento.")


while True:
    print("\n1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Buscar por autor")
    print("5. Libros disponibles")
    print("6. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_libro(biblioteca)
    elif opcion == "2":
        prestar_libro(biblioteca)
    elif opcion == "3":
        devolver_libro(biblioteca)
    elif opcion == "4":
        buscar_por_autor(biblioteca)
    elif opcion == "5":
        libros_disponibles(biblioteca)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")

"""
¿Por qué buscar_por_autor y libros_disponibles usan list comprehension?
Tu versión usaba una bandera encontrado = False para saber si había resultados. La comprehension construye la lista primero y luego checas si está vacía — más limpio y sin bandera:
python# Tu versión — bandera manual
encontrado = False
for nombre, datos in biblioteca.items():
    if datos['autor'] == autor:
        print(...)
        encontrado = True
if not encontrado:
    print("No encontrado")

# Con comprehension — sin bandera
resultado = [(n, d) for n, d in biblioteca.items() if d["autor"] == autor]
if resultado:
    for nombre, datos in resultado:
        print(...)
else:
    print("No encontrado")

"""