# nhap mang
arr = list(map(int, input("nhap mang cac so tu nhien(cach nhau bang dau cach): ").split()))

# ham kiem tra so nguyen to
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# so le

odd_numbers = [x for x in arr if x % 2 != 0]
print("cac so le: ", odd_numbers, "- tong:", len(odd_numbers))

# so nguyen to
prime_numbers = [ x for x in arr if is_prime(x)]
print("cac so nguyen to: ", prime_numbers)



