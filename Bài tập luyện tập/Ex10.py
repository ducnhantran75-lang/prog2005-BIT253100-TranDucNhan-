filename = "products.txt"

def add_product():
    code = input("Code: ")
    name = input("Name: ")
    price = float(input("Price: "))

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")


def show_products():
    products = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            code, name, price = line.strip().split(";")
            products.append((code, name, float(price)))

    print("Danh sách sản phẩm:")
    for p in products:
        print(p)

    print("\nSắp xếp giá giảm dần:")
    products.sort(key=lambda x: x[2], reverse=True)

    for p in products:
        print(p)


add_product()
show_products()
