class Product:
    def __init__(self, price):
        self.set_price(price)

    # setter
    def set_price(self, price):
        if price < 0:
            print("Lỗi: Giá không được âm!")
        else:
            self._price = price

    # getter
    def get_price(self):
        return self._price

p = Product(100)
print("Giá:", p.get_price())

p.set_price(-50)  # lỗi