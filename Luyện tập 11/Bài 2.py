# Nhập danh sách chuỗi
arr = []
print("Nhập 5 chuỗi:")
for i in range(5):
    s = input(f"Chuỗi {i+1}: ")
    arr.append(s)

# Sắp xếp giảm dần theo độ dài
arr.sort(key=len, reverse=True)

print("\nDanh sách sau khi sắp xếp:")
for i in range(len(arr)):
    print(f"{i}: {arr[i]} (độ dài {len(arr[i])})")

# Nhập chuỗi cần tìm
target = input("\nNhập chuỗi cần tìm: ")
target_len = len(target)

# Binary Search theo độ dài
left = 0
right = len(arr) - 1
found = False

while left <= right:
    mid = (left + right) // 2
    mid_len = len(arr[mid])

    print(f"Đang xét vị trí {mid}: {arr[mid]}")

    if mid_len == target_len:
        # tìm đúng độ dài -> kiểm tra nội dung
        if arr[mid] == target:
            print(f"\n Tìm thấy tại vị trí {mid}")
            found = True
            break
        else:
            # nếu trùng độ dài nhưng khác chuỗi → tìm lân cận
            i = mid - 1
            while i >= left and len(arr[i]) == target_len:
                if arr[i] == target:
                    print(f"\n Tìm thấy tại vị trí {i}")
                    found = True
                    break
                i -= 1

            i = mid + 1
            while i <= right and len(arr[i]) == target_len:
                if arr[i] == target:
                    print(f"\n Tìm thấy tại vị trí {i}")
                    found = True
                    break
                i += 1

            break

    elif mid_len < target_len:
        right = mid - 1
    else:
        left = mid + 1

if not found:
    print("\nKhông tìm thấy chuỗi")