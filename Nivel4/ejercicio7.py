"""
Ejercicio 7 — Desafío
Crea una agenda de contactos completa usando diccionarios. Implementa cuatro funciones:
 agregar_contacto, buscar_contacto, eliminar_contacto y mostrar_agenda. Los contactos tienen nombre, teléfono y email.
1. Agregar contacto
2. Buscar contacto
3. Eliminar contacto
4. Mostrar agenda
5. Salir
"""
"""
Opción: 1
Nombre: Ana
Teléfono: 555-1234
Email: ana@mail.com
Contacto agregado.
Opción: 2
Buscar: Ana
Nombre: Ana  |  Tel: 555-1234  |  Email: ana@mail.com

💡 Tip: usa get() en buscar_contacto y eliminar_contacto para manejar el caso donde el contacto no existe.
"""
agenda = {
   
}
def agregar_contacto(agenda):
    nombre=input("nombre:")
    telefono=input("telefono:")
    email=input("email:")
    agenda[nombre]={f"telefono":telefono,"email":email}
    print("Contacto agregado")

def buscar_contacto(agenda):
    nombre=input("Nombre: ")
    contacto=agenda.get(nombre)
    if contacto:
     print(f"Nombre: {nombre} | Tel: {contacto['telefono']} | Email: {contacto['email']}")
    else:
        print(f"'{nombre}' no encontrado.")
def eliminar_contacto(agenda):
    nombre = input("Eliminar: ")

    if agenda.get(nombre):         # checa si existe antes de eliminar
        agenda.pop(nombre)
        print(f"'{nombre}' eliminado.")
    else:
        print(f"'{nombre}' no encontrado.")

def mostrar_agenda(agenda):
    if not agenda:                 # diccionario vacío = False
        print("La agenda está vacía.")
        return

    for nombre, datos in agenda.items():
        print(f"{nombre} | Tel: {datos['telefono']} | Email: {datos['email']}")



while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar agenda")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        buscar_contacto(agenda)
    elif opcion == "3":
        eliminar_contacto(agenda)
    elif opcion == "4":
        mostrar_agenda(agenda)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")


#SOLUCION COMUN
def agregar_contacto(agenda):
    nombre   = input("Nombre: ")

    if nombre in agenda:
        print(f"'{nombre}' ya existe en la agenda.")
        return

    telefono = input("Teléfono: ")
    email    = input("Email: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print("Contacto agregado.")

def buscar_contacto(agenda):
    nombre   = input("Buscar: ")
    contacto = agenda.get(nombre)

    if contacto:
        print(f"Nombre: {nombre} | Tel: {contacto['telefono']} | Email: {contacto['email']}")
    else:
        print(f"'{nombre}' no encontrado.")

def eliminar_contacto(agenda):
    nombre = input("Eliminar: ")

    if agenda.get(nombre):
        agenda.pop(nombre)
        print(f"'{nombre}' eliminado.")
    else:
        print(f"'{nombre}' no encontrado.")

def mostrar_agenda(agenda):
    if not agenda:
        print("La agenda está vacía.")
        return

    print(f"\nAgenda ({len(agenda)} contactos):")
    for nombre, datos in agenda.items():
        print(f"  {nombre} | Tel: {datos['telefono']} | Email: {datos['email']}")


agenda = {}

while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar agenda")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_contacto(agenda)
    elif opcion == "2":
        buscar_contacto(agenda)
    elif opcion == "3":
        eliminar_contacto(agenda)
    elif opcion == "4":
        mostrar_agenda(agenda)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")