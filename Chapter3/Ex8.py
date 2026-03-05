numbers = list(map(int, input("Nhap danh sach so: ").split()))

found = None

for num in numbers:
    if num > 10:
        found = num
        break

if found:
    print("So dau tien lon hon 10:", found)
else:
    print("Khong co so nao lon hon 10")
