# Nhập 5 chuỗi
arr = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    arr.append(s)

print("\nDanh sách ban đầu:", arr)

# Insertion Sort giảm dần theo độ dài
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    print(f"\n--- Bước {i} ---")
    print("Key đang xét:", key)

    # So sánh độ dài (giảm dần)
    while j >= 0 and len(arr[j]) < len(key):
        arr[j + 1] = arr[j]
        j -= 1
        print("Sau khi dịch:", arr)

    arr[j + 1] = key
    print("Sau khi chèn:", arr)

print("\nKết quả cuối cùng:", arr)
