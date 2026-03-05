colors = ["Red", "Blue", "Green", "Yellow", "Black"]

try:
    colors.remove("Green")
except ValueError:
    print("Khong tim thay mau Green")

print("Danh sach sau khi xoa:", colors)
