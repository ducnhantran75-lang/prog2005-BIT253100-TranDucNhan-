numbers = list(map(int, input("Nhap danh sach so: ").split()))

print("Cac so le:")

for num in numbers:
    if num % 2 != 0:
        print(num)
