class Inventario():
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Error: Ya existe un producto con este ID.")
        else:
            self.productos[producto.id] = producto
            print("Producto agregado exitosamente.")
    
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado exitosamente.")
        else:
            print("Error: No existe un producto con este ID.")
    
    def actualizar_producto(self, id, nombre=None, descripcion=None, cantidad=None, precio=None):
        if id in self.productos:
            if nombre:
                self.productos[id].actualizar_nombre(nombre)
            if descripcion:
                self.productos[id].actualizar_descripcion(descripcion)
            if cantidad is not None:
                self.productos[id].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id].actualizar_precio(precio)
            print("Producto actualizado exitosamente.")
        else:
            print("Error: No existe un producto con este ID.")

    def buscar_producto(self, id):
        if id in self.productos:
            print(self.productos[id])
        else:
            print("Producto no encontrado.")
    
    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print('Tienes estos productos en tu inventario:\n')
            for producto in self.productos.values():
                print(producto)
