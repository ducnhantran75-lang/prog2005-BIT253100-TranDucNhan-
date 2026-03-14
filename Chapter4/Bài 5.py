class Product:

    def __init__(self,price):
        self.set_price(price)

    # setter
    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Gia phai lon hon 0")


    #getter
    def get_price(self):
        return self._price

    # in thong tin
    def __str__(self):
        return f"Price: {self._price}"

p1 = Product(1150)
print(p1)
