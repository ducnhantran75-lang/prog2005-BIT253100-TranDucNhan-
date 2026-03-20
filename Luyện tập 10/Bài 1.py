import os
def lay_ten_file(path):
    return os.path.basename(path)

def lay_ten_khong_duoi(path):
    return os.path.splitext(os.path.basename(path))[0]

p = input("nhap link bai hat")
print(lay_ten_file(p))
print(lay_ten_khong_duoi(p))

