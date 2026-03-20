so_lan = 0

while so_lan <5:
    mat_khau = input("nhap mat khau: ")

    if mat_khau == "python123":
        print("dang nhap thanh cong!")
        break
    else:
        print("mat khau sai!")
        so_lan += 1

if so_lan == 5:
    print("ban da nhap qua 5 lan!")


