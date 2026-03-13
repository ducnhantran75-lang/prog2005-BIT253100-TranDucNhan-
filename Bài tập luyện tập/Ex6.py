s = input("Nhap chuoi so:")

nums = [int(x.strip())for x in s.split(";")]

for n in nums:
    print(n)

even = sum(1 for n in nums if n % 2 == 0)
negative = sum(1 for n in nums if n <0)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n & i == 0:
            return False
        return True

prime = sum(1 for n in nums if is_prime(n))

avg = sum(nums) / len(nums)

print("so chan:", even)
print("so am:", negative)
print("so nguyen to:", prime)
print("trung binh:", avg)s = input("Nhap chuoi so:")

nums = [int(x.strip())for x in s.split(";")]

for n in nums:
    print(n)

even = sum(1 for n in nums if n % 2 == 0)
negative = sum(1 for n in nums if n <0)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n & i == 0:
            return False
        return True

prime = sum(1 for n in nums if is_prime(n))

avg = sum(nums) / len(nums)

print("so chan:", even)
print("so am:", negative)
print("so nguyen to:", prime)
print("trung binh:", avg)
