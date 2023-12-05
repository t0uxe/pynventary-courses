class Inventary:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def delete_product(self, id):
        for i, product in enumerate(self._products):
            if product.id == id:
                self._products.remove(self._products[i])
                print("Producto borrado.")
                break
        else:
            print("Producto no encontrado.")
            
    def update_product(self, id, new_quantity=None, new_price=None):
        for product in self._products:
            if id == product.id:
                product.quantity = new_quantity if new_quantity is not None else product.quantity
                product.price = new_price if new_price is not None else product.price
                print("Producto actualizado.")
                break
        else:
            print("Producto no encontrado.")

    def __str__(self):
        return "".join((f"ID: {p.id}\nNombre: {p.name}\nCantidad: {p.quantity}\nPrecio: {p.price}\n\n" for p in self._products))


    def total_value(self):
        """Sumatorio de la cantidad de producto por su precio, por todos los productos del inventario."""
        return sum([product.quantity * product.price for product in self._products])

    def total_products(self):
        return len(self._products)