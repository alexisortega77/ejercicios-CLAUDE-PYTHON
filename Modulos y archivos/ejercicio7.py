"""
Ejercicio 7 — Desafío
Crea un sistema de contacts de contactos persistente. Los contactos se guardan en 
JSON y el menú permite agregar, buscar, eliminar y listar. Los cambios persisten entre ejecuciones.
1. Add contact
2. Search contact
3. Delete contact
4. List all
5. Exit

# Los datos se cargan al iniciar y se guardan al salir

"""
import json

FILENAME = "contacts.json"

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(contacts, filename):
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Name: ").strip()
    if name in contacts:
        print(f"'{name}' already exists.")
        return
    contacts[name] = {
        "phone": input("Phone: ").strip(),
        "email": input("Email: ").strip()
    }
    save_data(contacts, FILENAME)
    print("Contact added.")

def search_contact(contacts):
    query   = input("Search: ").strip().lower()
    results = {
        name: data for name, data in contacts.items()
        if query in name.lower()
    }
    if results:
        for name, data in results.items():
            print(f"  {name} | Phone: {data['phone']} | Email: {data['email']}")
    else:
        print(f"No contacts found for '{query}'.")

def delete_contact(contacts):
    name = input("Delete: ").strip()
    if name in contacts:
        contacts.pop(name)
        save_data(contacts, FILENAME)
        print(f"'{name}' deleted.")
    else:
        print(f"'{name}' not found.")

def list_all(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    print(f"\nContacts ({len(contacts)}):")
    for name, data in sorted(contacts.items()):   # ordenados alfabéticamente
        print(f"  {name:<15} | {data['phone']:<15} | {data['email']}")


contacts = load_data(FILENAME)

MENU = {
    "1": ("Add contact",    lambda: add_contact(contacts)),
    "2": ("Search contact", lambda: search_contact(contacts)),
    "3": ("Delete contact", lambda: delete_contact(contacts)),
    "4": ("List all",       lambda: list_all(contacts)),
}

while True:
    print()
    for key, (label, _) in MENU.items():
        print(f"{key}. {label}")
    print("5. Exit")

    option = input("Option: ")

    if option in MENU:
        MENU[option][1]()
    elif option == "5":
        print("See you soon!")
        break
    else:
        print("Invalid option.")