a = float(input("nhap diem mon thu nhat: "))
b = float(input("nhap diem mon thu hai: "))
c = float(input("nhap diem mon thu ba: "))

trung_binh = (a+b+c)/3
print("diem trung binh la: ")
if trung_binh >= 8:
    print("ban thuoc loai gioi!")
elif trung_binh >= 6.5:
    print("ban thuoc loai kha!")
elif trung_binh >= 5.0:
    print("ban thuoc loai tb!")
elif trung_binh < 5.0:
    print("ban thuoc loai yeu!")

