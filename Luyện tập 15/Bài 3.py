
def giai_thua(n):
    if n == 0 or n == 1:   # điều kiện dừng
        return 1
    else:
        return n * giai_thua(n - 1)


n = int(input("Nhập số nguyên n: "))


if n < 0:
    print("Không tồn tại giai thừa cho số âm")
else:
    print("Giai thừa của", n, "là:", giai_thua(n))