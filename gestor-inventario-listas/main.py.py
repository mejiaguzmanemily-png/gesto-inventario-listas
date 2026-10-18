productos = []
cantidades = []

def registrar_producto():
    print("\n---REGISTRAR PRODUCTO---")
    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre del producto no puede estar vacion.")
        return
    posicion = -1
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            posicion = i
            break

    if posicion != -1:
        print(f"El producto {productos[posicion]} y existe en el inventario.")
        opcion = input("¿Desea sumar la nueva cantidad a la existente? (si/no): ").strip().lower()
        if opcion == "si":
            try:
                adicional = int(input("Cantidad a agregar: "))
                if adicional > 0:
                    cantidades[posicion] += adicional
                    print(f"Cantidad actializada. Nueva cantidad de {productos[posicion]}:  {cantidades[posicion]}")
                else:
                    print("La cantidad no puede ser negativa.")
            except ValueError:
                    print("Debe ingresar un número entero valido")
    else:
        try:
            cantidad = int(input("Cantidad inicial disponible: "))
            if cantidad >= 0:
                productos.append(nombre)
                cantidades.append(cantidad)
                print(f"Producto {nombre} registrado exitosamente con {cantidad} unidades")
            else:
                print("La cantidad no puede ser negativa")
        except ValueError:
            print("Debe ingresar un número entero válido para la cantidad")
def mostrar_inventario():
    print("\n---Inventario---")
    if len(productos) == 0:
        print("El inventario esta vacio.")
    else: 
        for i in range(len(productos)):
            print(f"{i + 1}. {productos[i]} - {cantidades[i]} unidades")

def buscar_producto():
    print("\n---Buscar Producto---")
    if len(productos) == 0:
        print("El inventario esta vacio")
        return
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    posicion = -1

    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            posicion = i 
            break
    if posicion != -1:
        print(f"Producto encontrado: {productos[posicion]}. Cantidad disponible: {cantidades[posicion]}")
    else:
        print(f"El producto {nombre} no se encuentra registrado en el inventario.")

def modificar_cantidad():
    print("\n---Modificar Cantidad---")
    if len(productos) == 0:
        print("El inventario esta vacio.")
        return

    nombre = input("Ingrese el nombre dle producto a modificar: ").strip()
    posicion = -1

    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            posicion = i
            break
    if posicion != -1:
        print(f"Producto seleccionado: {productos[posicion]}. Cantidad actual: {cantidades[posicion]}")
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            if nueva_cantidad >= 0:
                cantidades[posicion] = nueva_cantidad
                print("Cantidad modificada exitosamente.")
            else:
                print("La cantidad no puede ser negativa.")
        except ValueError:
            print("Debe ingresar un número entero válido.")
    else:
        print(f"No se encontró el producto {nombre}.")

def eliminar_producto():
    print("\n---Eliminar Producto---")
    if len(productos) == 0:
        print("El inventario esta vacio.")
        return
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    posicion = -1

    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            posicion = i
            break
    if posicion != -1:
        producto_eliminado = productos.pop(posicion)
        cantidad_eliminado = cantidades.pop(posicion)
        print(f"Se ha eliminado el producto {producto_eliminado} que tenia {cantidad_eliminado} unidades.")
    else:
        print(f"No se encontro el producto {nombre}")
def resumen_inventario():
    print("\n---Resumen Del Inventario---")
    total_diferentes = len(productos)
    print(f"Total de productos diferentes registrados: {total_diferentes}") 

    if total_diferentes > 0:
        mayor_cantidad = max(cantidades)
        posicion_mayor = cantidades.index(mayor_cantidad)
        print(f"Producto con mayor cantidad disponible: {productos[posicion_mayor]} con {mayor_cantidad} unidades.")
    else: 
        print("El inventario esta vacion, no hay estadisticas disponibles")
def menu():
    while True:
        print("\n====================")
        print(" GESTOR DE INVENTARIO - MENU")    
        print("====================")
        print("1. Registrar un producto")
        print("2. Mostrar inventario completo")   
        print("3. Buscar un producto")   
        print("4. Modificar cantidad de un producto")   
        print("5. Eliminar un producto")   
        print("6. Mostrar cantidad de productos diferentes")
        print("7. Mostrar producto con mayor cantidad")
        print("8. Salir")         
        print("====================")

        opcion = input("Seleccione una opcion (1-8): ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print(f"\nProductos diferentes en registro: {len(productos)}")
        elif opcion == "7":
            if len(productos) == 0:
                print("\nEl inventario esta vacio")
            else:
                mayor = max(cantidades)
                pos = cantidades.index(mayor)
                print(f"\nProducto con mayor stock: {productos[pos]}.  {mayor} unidades")
        elif opcion == "8":
            print("\n¡Gracias por utilizar el gestor de inventario!")
            break
        else:
            print("\nOpcion no valida. Seleccione un numero de 1 a 8")
if __name__ == "__main__":
    menu()