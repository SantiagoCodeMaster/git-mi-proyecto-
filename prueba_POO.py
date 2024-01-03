#iniciamos la clase producto para establecer los atributos del cualquier producto
class Producto:
  def __init__(self,nombre,precio,stock):
    self.nombre = nombre 
    self.precio = precio
    self.stock = stock
 

# Creamos la clase hija para iniciar los métodos con los atributos que hereda de la clase padre Producto
class Tienda(Producto):
    def __init__(self, nombre, precio, stock):
        super().__init__(nombre,precio,stock)
        self.inventario = []

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.inventario.append(producto)
            return(f"Producto '{producto.nombre}' agregado a la tienda.")
        else:
            return("El objeto no es una instancia de la clase Producto y no puede ser agregado")

    def realizar_compra(self,producto,stock):
      return (f"el usuario realiza la compra de {producto}  y compra {stock} de ellos")
      return (f"el usuario realiza la compra de {producto} y compra {stock} de ellos") 
      inventario_nuevo = self.inventario.remove([stock])
      



store = Tienda("producto",000,000)
producto1 = Producto("gasesosa coca cola",2.500,230)
producto2 = Producto("gaseosa postobon",3.500,230)
producto3 = Producto("perro",5.000,102)

print(store.agregar_producto(producto1))
print(store.agregar_producto(producto2))
print(store.agregar_producto(producto3))
print(store.realizar_compra("perro",2))
print(store.realizar_compra("gaseosa postobon",1))