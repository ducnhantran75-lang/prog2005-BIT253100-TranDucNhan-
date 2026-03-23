# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 1. Khởi tạo danh sách
numbers = list(map(int, input("Nhập danh sách số nguyên: ").split()))
print("Danh sách ban đầu:", numbers)

# 2. Thêm phần tử
x = int(input("Nhập số cần thêm: "))
numbers.append(x)
print("Sau khi thêm:", numbers)

# 3. Nhập k và đếm số lần xuất hiện
k = int(input("Nhập k: "))
count_k = numbers.count(k)
print(f"Số lần xuất hiện của {k}:", count_k)

# 4. Tính tổng các số nguyên tố
prime_sum = 0
for num in numbers:
    if is_prime(num):
        prime_sum += num
print("Tổng các số nguyên tố:", prime_sum)

# 5. Sắp xếp danh sách (tăng dần)
numbers.sort()
print("Danh sách sau khi sắp xếp:", numbers)

# 6. Xóa danh sách
numbers.clear()
print("Danh sách sau khi xóa:", numbers)