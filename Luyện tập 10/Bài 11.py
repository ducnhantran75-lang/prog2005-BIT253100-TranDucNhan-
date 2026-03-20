# ====== Các hàm bài tập ======

def bai1():
    path = input("Nhập đường dẫn: ")
    path = path.replace("\\", "/")
    ten_file = path.split("/")[-1]
    ten = ten_file.rsplit(".", 1)[0]
    print("Tên file:", ten_file)
    print("Tên không đuôi:", ten)

def bai2():
    s = input("Nhập chuỗi: ")
    k = input("Nhập ký tự: ")
    print("Số lần xuất hiện:", s.count(k))

def bai3():
    def giai_thua(n):
        if n <= 1:
            return 1
        return n * giai_thua(n - 1)

    n = int(input("Nhập n: "))
    if n < 0:
        print("Không hợp lệ!")
    else:
        print("Giai thừa:", giai_thua(n))

def bai4():
    s = input("Nhập chuỗi: ")
    if s.strip() == "":
        print("Chuỗi rỗng!")
    else:
        print("Độ dài:", len(s))

def bai6():
    s = input("Nhập chuỗi: ")
    dao = ""
    for c in s:
        dao = c + dao
    print("Chuỗi đảo:", dao)

# ====== MENU ======
while True:
    print("\n===== MENU =====")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("6. Bài 6")
    print("0. Thoát")

    chon = input("Chọn bài: ")

    if chon == "1":
        bai1()
    elif chon == "2":
        bai2()
    elif chon == "3":
        bai3()
    elif chon == "4":
        bai4()
    elif chon == "6":
        bai6()
    elif chon == "0":
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")