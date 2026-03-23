import csv

name = input("Nhập tên: ")
age = input("Nhập tuổi: ")
emp_id = input("Nhập ID: ")

# Ghi file TXT
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {name}\nTuổi: {age}\nID: {emp_id}")

# Ghi file CSV
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerow([name, age, emp_id])

print("Đã lưu file thành công!")