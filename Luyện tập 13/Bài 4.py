def tong(n):
    if n == 1:
        return 1
    return n + tong(n - 1)

n = int(input("nhap n :"))
print("tong tu 1 den n la:", tong(n))