class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # Getter
    def get_price(self):
        return self._price

    # Setter
    def set_price(self, price):
        self._price = price

# Tạo object
book = Book("Book 1", 30000)

# In giá
print("Giá sách:", book.get_price())