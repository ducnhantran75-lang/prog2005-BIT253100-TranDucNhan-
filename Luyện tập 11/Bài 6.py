# Khởi tạo dictionary
people = {}

n = int(input("Nhập số người: "))

for i in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    people[name] = age

# Tính tuổi trung bình
total_age = sum(people.values())
avg_age = total_age / len(people)

print("Danh sách:", people)
print("Tuổi trung bình:", avg_age)