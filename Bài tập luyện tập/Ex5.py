import random

m = int(input("Nhap so hang:"))
n = int(input("Nhap so cot"))
matrix = [[random.randint(1, 101) for j in range(n)] for i in range(m)]
print("Ma tran:")
for row in matrix:
    print(row)

# hien thi hang
r = int(input("Nhap hang muon xem: "))
print(matrix[r-1])

# hien thi cot
c = int(input("Nhap cot muon xem: "))
for row in matrix:
    print(row[c-1])

# tim max
max_val = max(max(row) for row in matrix)
print("Gia tri lon nhat:", max_val)
