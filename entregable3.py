ask= True
# Diccionario de productos de supermercado
productos = {
    "manzanas": {"precio": 1200, "cantidad": 50},
    "pan": {"precio": 800, "cantidad": 30},
    "leche": {"precio": 1500,"cantidad": 20},
    "huevos": {"precio": 2500, "cantidad": 10},
    "arroz": {"precio": 900, "cantidad": 40},
    "pollo": {"precio": 5000, "cantidad": 15},
    "papel higiénico": {"precio": 3000, "cantidad": 25},
    "jugo": {"precio": 2000, "cantidad": 18},
    "queso": {"precio": 4000, "cantidad": 12},
    "cereal": {"precio": 3500, "cantidad": 8}
}

# Lista para almacenar el historial de movimientos
historial_movimientos = []

def registrar_movimiento(accion, producto, detalles):
    """
    Registra un movimiento en el historial.
    :param accion: Acción realizada (Agregar, Actualizar, Eliminar).
    :param producto: Nombre del producto afectado.
    :param detalles: Detalles adicionales del movimiento.
    """
    movimiento = (accion, producto, detalles)
    historial_movimientos.append(movimiento)

def ver_historial():
    """
    Muestra el historial de movimientos realizados.
    """
    print("\nHistorial de movimientos:")
    if not historial_movimientos:
        print("No hay movimientos registrados.")
    else:
        for idx, movimiento in enumerate(historial_movimientos, start=1):
            accion, producto, detalles = movimiento
            print(f"{idx}. Acción: {accion}, Producto: {producto}, Detalles: {detalles}")

def menu():
    print("Bienvenido al supermercado")
    print("1. Agregar productos")
    print("2. Actualizar productos")
    print("3. Eliminar productos")
    print("4. Ver productos")
    print("5. Ver historial de movimientos")
    print("6. Salir")
    opcion =int(input("Seleccione una opción: "))
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        actualizar_producto()
    elif opcion == 3:
        eliminar_producto()
    elif opcion == 4:
        ver_productos()
    elif opcion == 5:
        ver_historial()
    elif opcion == 6: 
        print("Gracias por usar el sistema de supermercado.")
        exit()
    else:
        print("Opción no válida. Intente nuevamente.")
        menu()
def ver_productos():
    print("Productos disponibles:")
    for producto, info in productos.items():
        print(f"{producto.capitalize()}: Precio: ${info['precio']}, Cantidad: {info['cantidad']}")

def agregar_producto():
    while ask:
        nombre = input("Ingrese el nombre del producto: ").lower()
        if nombre in productos:
            print("El producto ya existe.")
        else:
            precio = int(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            productos[nombre] = {"precio": precio, "cantidad": cantidad}
            print(f"Producto {nombre} agregado con éxito.")
            registrar_movimiento("Agregar", nombre, f"Precio: {precio}, Cantidad: {cantidad}")
        agregar_mas = input("¿Desea agregar otro producto? (si/no): ").lower()
        if agregar_mas != "si":
            ask = False
        menu()
    
def actualizar_producto():
    print("Qué producto desea actualizar?")
    ver_productos()
    while ask:
        nombre = input("Ingrese el nombre del producto: ").lower()
        if nombre in productos:
            precio = int(input("Ingrese el nuevo precio del producto: "))
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            productos[nombre] = {"precio": precio, "cantidad": cantidad}
            print(f"Producto {nombre} actualizado con éxito.")
            registrar_movimiento("Actualizar", nombre, f"Nuevo precio: {precio}, Nueva cantidad: {cantidad}")
            print("¿Desea actualizar otro producto?")
            agregar_mas = input("¿Desea actualizar otro producto? (si/no): ").lower()
            if agregar_mas != "si":
                ask = False
                menu()
        else:
            print("El producto no existe.")
            print("¿Desea agregarlo?")
            agregar = input("Ingrese 'si' para agregar el producto o 'no' para volver al menú: ").lower()
            if agregar == "si":
                agregar_producto()
            else:
                menu()

def eliminar_producto():
    print("Qué producto desea eliminar?")
    ver_productos()
    nombre = input("Ingrese el nombre del producto: ").lower()
    if nombre in productos:
        del productos[nombre]
        print(f"Producto {nombre} eliminado con éxito.")
        registrar_movimiento("Eliminar", nombre, "Producto eliminado del inventario")
        print("¿Desea eliminar otro producto?")
        agregar_mas = input("¿Desea eliminar otro producto? (si/no): ").lower()
        if agregar_mas != "si":
            ask = False
            menu()
    else:
        print("El producto no existe.")
        menu()

