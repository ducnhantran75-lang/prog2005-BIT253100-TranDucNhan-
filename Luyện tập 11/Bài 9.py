# Nhập kích thước
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))

A = []
B = []

print("Nhập ma trận A:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = input(f"A[{i}][{j}] = ")
        if val == "":
            print("Lỗi: Không được nhập rỗng!")
            exit()
        row.append(int(val))
    A.append(row)

print("Nhập ma trận B:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = input(f"B[{i}][{j}] = ")
        if val == "":
            print("Lỗi: Không được nhập rỗng!")
            exit()
        row.append(int(val))
    B.append(row)

# Cộng ma trận
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# In kết quả
print("Ma trận kết quả:")
for row in C:
    print(row)