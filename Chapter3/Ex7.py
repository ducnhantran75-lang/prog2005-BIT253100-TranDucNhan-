numbers = list(map(int, input("Nhap danh sach so: ").split()))
x = int(input("Nhap so can tim: "))

index = -1

for i in range(len(numbers)):
    if numbers[i] == x:
        index = i
        break

if index != -1:
    print("Tim thay tai vi tri:", index)
else:
    print("Khong tim thay")
