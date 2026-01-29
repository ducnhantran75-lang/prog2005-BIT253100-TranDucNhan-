try:
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    print("Kết quả:", a / b)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")
except ValueError:
    print("Lỗi: Dữ liệu nhập không hợp lệ")
