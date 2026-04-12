'''Inventario:
- Laptop:   $15000  x 3  = $45000
- Mouse:    $350    x 10 = $3500
- Teclado:  $800    x 5  = $4000
Valor total del inventario: $52500'''

inventario={}

def agregar_producto(nombre, precio, cantidad):
    inventario[nombre]={
        "precio": precio,
        "cantidad":cantidad        
    }
    return
def mostrar_inventario():
    for nombre, datos in inventario.items():
        precio=datos["precio"]
        cantidad=datos["cantidad"]
        precio_stock_producto=precio*cantidad
        print(f"{nombre}: ${precio} x {cantidad}= {precio_stock_producto}")
    return
def calcular_inventario_total():
    total_inventario=0
    for datos in inventario.values():
        total_inventario+=datos["precio"]*datos["cantidad"]
    print(f"el total del inventario es de: {total_inventario}")
    return

agregar_producto("playstation", 10000, 3)
agregar_producto("xbox one", 4000, 9)
agregar_producto("psp", 3000, 2)
agregar_producto("laptop", 17000, 6)
mostrar_inventario()
calcular_inventario_total()