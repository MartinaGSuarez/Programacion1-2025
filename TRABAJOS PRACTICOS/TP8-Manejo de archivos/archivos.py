# Trabajo practico 6
# Manejo de archivos

# == ACTIVIDAD 1 ==

'''
lapiz,200.0,45
regla,120.50,26
corrector,100.0,25
'''

# == ACTIVIDAD 2 ==
def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.split(",")
            print(f"Producto: {nombre}, Precio: ${precio}, Cantidad: {cantidad}")

# == ACTIVIDAD 3 ==
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese ña cantidad del producto: "))
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("producto agregado correctamente.\n")

# == ACTIVIDAD 4 == 
def cargar_productos_en_una_lista():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)}
            productos.append(producto)
    return productos

# == ACTIVIDAD 5 ==
def buscar_producto(productos):
    nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print(f"Producto encontrado: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

# == ACTIVIDAD 6 ==
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n"
            archivo.write(linea)
    print("Productos guardados correctamente.")

