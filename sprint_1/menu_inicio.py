'''
Implemente una menú de usuario que permita a los usuarios interactuar con el sistema de gestión de inventario. 
El menú de incluir opciones para realizar las diferentes operaciones disponibles en la clase Inventario. Utilice
un bucle while y estructuras de control de flujo if-elif-else para manejar las diferentes opciones del 
menú. (opcional)
4. Asegúrese de que el sistema maneje adecuadamente errores y excepciones, como entradas inválidas del usuario 
o intentos de actualizar o eliminar productos que no existen en el inventario.
'''

# Modulos
from productos_1 import Producto
from inventario_2 import Inventario

# Menu
def menu():
    inventario = Inventario()  # Asume que la clase Inventario ya está definida

    while True:
        print("-"*80)
        print("Menú del Sistema de Gestión de Inventario")
        print("-"*80)
        print("\n1. Agregar producto al inventario")
        print("2. Eliminar producto del inventario")
        print("3. Actualizar producto en el inventario")
        print("4. Buscar un producto en el inventario")
        print("5. Listar todos los productos en el inventario")
        print("6. Salir")

        opcion = input("\nPor favor, selecciona una opción: ")

        if opcion == "1":
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            try:
                cantidad = int(input("Cantidad del producto: "))
                precio = int(input("Precio del producto: "))
                producto = Producto(id, nombre, descripcion, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: La cantidad y/o el precio deben ser números enteros.")

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            nombre = input("Nuevo nombre (deja en blanco si no quieres cambiarlo): ")
            descripcion = input("Nueva descripción (deja en blanco si no quieres cambiarla): ")
            cantidad = input("Nueva cantidad (deja en blanco si no quieres cambiarla): ")
            precio = input("Nuevo precio (deja en blanco si no quieres cambiarlo): ")
            inventario.actualizar_producto(id, nombre, descripcion, cantidad, precio)

        elif opcion == "4":
            id = input("ID del producto a buscar: ")
            inventario.buscar_producto(id)

        elif opcion == "5":
            inventario.listar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


menu()
