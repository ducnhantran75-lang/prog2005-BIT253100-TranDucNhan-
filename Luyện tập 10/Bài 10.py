# Nhập 5 chuỗi
ds = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i + 1}: ")
    ds.append(s)

n = len(ds)

print("\nCác bước sắp xếp:")

# Bubble Sort (giảm dần theo độ dài)
for i in range(n - 1):
    for j in range(n - i - 1):
        if len(ds[j]) < len(ds[j + 1]):
            # Hoán đổi
            ds[j], ds[j + 1] = ds[j + 1], ds[j]

            # In sau mỗi lần đổi
            print(ds)

print("\nKết quả cuối cùng:", ds)