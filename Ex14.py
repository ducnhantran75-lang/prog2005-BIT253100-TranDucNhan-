import math

number = float(input("Nhập số: "))

if number >= 0:
    print("Căn bậc hai:", math.sqrt(number))
else:
    print("Lỗi: Không thể tính căn bậc hai của số âm")
