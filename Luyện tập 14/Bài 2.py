names = []

# nhap 5 ten
for i in range(5):
    name = input(f"nhap ten thu {i+1}: ")
    names.append(name)

print("danh sach ban dau:", names)

# xoa phan tu thu 2
del names[1]

print("danh sach sau khi xoa:", names)

