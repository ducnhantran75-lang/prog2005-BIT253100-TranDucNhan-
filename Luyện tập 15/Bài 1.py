from stringprep import b3_exceptions
a = int(input ("nhap mot so a: "))
b = int(input ("nhap mot so b: "))
# tinh toan
tong = a+b
hieu = a-b
tich = a*b
if b != 0:
    thuong = a / b
else:
     print(" khong the chia cho 0 ")
# in ra
print("tong: ", tong)
print("hieu: ", hieu)
print("tich: ", tich)
print("thuong: ", thuong)
