chuoi = input("nhap chuoi: ")
ky_tu = input("nhap 1 ky tu: ")

if len(ky_tu) != 1:
    print("vui long nhap mot ky tu!: ")
else:
    print("so lan xuat hien: ", chuoi.count(ky_tu))

