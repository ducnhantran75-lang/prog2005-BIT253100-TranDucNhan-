num = input("nhap mot so: ")

total = 0
for digit in num:
    if digit.isdigit():
        total += int(digit)

print("tong cac chu so la:", total)
