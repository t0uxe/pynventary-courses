import uuid

class Product:
    def __init__(self, name, quantity, price):
        self.id = str(uuid.uuid4())
        self._name = name
        self._quantity = quantity
        self._price = price
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        max_length_name = 30
        if len(new_name) > max_length_name:
            print(f"Nombre de producto demasiado larga. Por favor, indique un nombre por debajo de {max_length_name} caracteres.")
        else:
            self._name = new_name

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):
        if new_quantity < 0 or not isinstance(new_quantity, int):
            print("Por favor, indique una cantidad correcta.")
        else:
            self._quantity = new_quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, (int, float)):
            self._price = float(new_price)
        else:
            print("Por favor, indique un precio correcto.")  