class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
product.price = 42
print(product.price)
