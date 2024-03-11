class Producto():
    def __init__(self, id, nombre, descripcion, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"|ID: {self.id}|Nombre: {self.nombre}|Descripción: {self.descripcion}|Cantidad: {self.cantidad}|Precio: ${self.precio}"
    
    # Métodos para modificar la información del producto
    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def actualizar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
        
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio



