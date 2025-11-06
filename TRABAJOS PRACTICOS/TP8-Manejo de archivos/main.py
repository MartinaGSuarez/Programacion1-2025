import archivos as a

while True:
    print("\n====== MENU ======")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = int(input("Elige una opcion: "))

    if opcion == "1":
        a.mostrar_productos()
    elif opcion == "2":
        a.agregar_producto()
    elif opcion == "3":
        productos = a.cargar_productos_en_lista()
        a.buscar_producto(productos)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
