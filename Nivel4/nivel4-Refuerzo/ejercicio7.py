"""
Ejercicio 7 — Desafío
Crea un sistema de biblioteca. Los libros son diccionarios con título, autor y disponible (True/False).
 Implementa funciones para agregar libro, prestar libro, devolver libro, buscar por autor y mostrar todos los libros disponibles.
1. Agregar libro
2. Prestar libro
3. Devolver libro
4. Buscar por autor
5. Libros disponibles
6. Salir

Opción 1:
Título: El principito
Autor: Saint-Exupéry
Libro agregado.

Opción 2:
Título: El principito
'El principito' prestado exitosamente.

Opción 5:
Libros disponibles: ninguno en este momento.
"""
biblioteca = {
}

def mostrar_disponible(valor):
    return "Si" if valor else "No"    

def agregar_libro(biblioteca):
  
        nombre_libro=input("Ingresa nombre de libro:").lower().strip() 
        nombre_autor=input("Ingrese nombre del autor: ").lower().strip() 
        disponible=True
        biblioteca[nombre_libro] = {"autor": nombre_autor, "disponible": disponible}

def libros_disponibles(biblioteca):
     hay_disponible=False
     for nombre, datos in biblioteca.items():

       if datos['disponible']:
         if not hay_disponible:
           print("Libros disponibles:")          
         print(f"Nombre libro: {nombre} | Autor: {datos["autor"]} | Disponible: {mostrar_disponible(datos['disponible'])}")
         hay_disponible=True
     if not hay_disponible:
            print("Libros disponibles: Ninguno en estos momentos")

def prestar_libro(biblioteca):
     nombre_libro=input("Titulo: ").lower()
     print(nombre_libro)
     encontrado=biblioteca.get(nombre_libro)
     if encontrado:
      if biblioteca[nombre_libro]["disponible"]:
    
       biblioteca[nombre_libro]["disponible"] = False
       print(f"El libro {nombre_libro} ha sido prestado exitosamente")
      else:
         print(f"{nombre_libro} ya ha sido prestado.")

     else:
        print(f"'{nombre_libro}' no encontrado.")

def devolver_libro(biblioteca):
     nombre_libro=input("Nombre del libro a devoler: ").lower().strip() 
     encontrado=biblioteca.get(nombre_libro)
     if encontrado:
      if not biblioteca[nombre_libro]["disponible"]:
    
       biblioteca[nombre_libro]["disponible"] = True
       print(f"El libro {nombre_libro} ha sido devuelto exitosamente")
      else:
         print(f"{nombre_libro} este libro no ha sido prestado.")

     else:
        print(f"'{nombre_libro}' no existe.")

def buscar_por_autor(biblioteca):
    nombre_autor=input("Ingresa autor: ").lower().strip() 
    encontrado = False
    for nombre, datos in biblioteca.items():
     if datos['autor'] == nombre_autor:
            print(f"Nombre libro: {nombre} | Autor: {datos["autor"]} | Disponible: {mostrar_disponible(datos['disponible'])}")
            encontrado=True
            
    if not encontrado:
        print("Libro no encontrado")

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
        break
    else:
        print("Opción inválida.")


