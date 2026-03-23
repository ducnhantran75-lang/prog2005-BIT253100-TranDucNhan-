# Nhập danh sách số
numbers = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))

even_numbers = []
total = 0

# Duyệt danh sách
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        total += num

# In kết quả
print("Các số chẵn:", even_numbers)
print("Tổng các số chẵn:", total)