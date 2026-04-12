
"""
**Ejercicio 5 — Medio**
Crea un programa que maneje un inventario de productos usando un diccionario. Cada producto tiene nombre, precio y cantidad. 
Implementa funciones para agregar producto, mostrar inventario y calcular el valor total del inventario.
```'
Inventario:
- Laptop:   $15000  x 3  = $45000
- Mouse:    $350    x 10 = $3500
- Teclado:  $800    x 5  = $4000
Valor total del inventario: $52500
``
"""
inventario={}
def producto(nombre, precio, cantidad):
    inventario[nombre]={
        "precio":precio,
        "cantidad":cantidad
    }
    return
def mostrar_inventario():
    for nombre,datos in inventario.items():
        precio=datos["precio"]
        cantidad=datos["cantidad"]
        total=precio*cantidad
        print(f"{nombre}: {precio} x {cantidad} = ${total}")
    return
def calcular_total():
    total_inventario=0
    for datos in inventario.values():
        total_inventario+=datos["precio"]*datos["cantidad"]
    print(f"Valor total del inventario: ${total_inventario}")
producto("Laptop", 15000, 3)
producto("Mouse", 350, 10)
producto("Teclado", 800, 5)

mostrar_inventario()
calcular_total()


#SOLUCION COMUN
def agregar_producto(inventario, nombre, precio, cantidad):
    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad
    }

def mostrar_inventario(inventario):
    print("Inventario:")
    for nombre, datos in inventario.items():
        precio   = datos["precio"]
        cantidad = datos["cantidad"]
        total    = precio * cantidad
        print(f"  - {nombre}: ${precio} x {cantidad} = ${total}")

def calcular_total(inventario):
    return sum(datos["precio"] * datos["cantidad"] for datos in inventario.values())


inventario = {}
agregar_producto(inventario, "Laptop",  15000, 3)
agregar_producto(inventario, "Mouse",   350,   10)
agregar_producto(inventario, "Teclado", 800,   5)

mostrar_inventario(inventario)
print(f"Valor total del inventario: ${calcular_total(inventario)}")



#SOLUCION OPTIMA
def agregar_producto(inventario, nombre, precio, cantidad):
    if precio < 0 or cantidad < 0:
        print("Error: precio y cantidad deben ser positivos.")
        return
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return

    print("Inventario:")
    for nombre, datos in inventario.items():
        precio   = datos["precio"]
        cantidad = datos["cantidad"]
        total    = precio * cantidad
        # ljust y rjust alinean el texto para que quede prolijo
        print(f"  - {nombre.ljust(10)} ${str(precio).rjust(6)}  x {str(cantidad).rjust(3)}  = ${total}")

def calcular_total(inventario):
    return sum(d["precio"] * d["cantidad"] for d in inventario.values())


inventario = {}
agregar_producto(inventario, "Laptop",  15000, 3)
agregar_producto(inventario, "Mouse",   350,   10)
agregar_producto(inventario, "Teclado", 800,   5)

mostrar_inventario(inventario)
print(f"\nValor total del inventario: ${calcular_total(inventario)}")