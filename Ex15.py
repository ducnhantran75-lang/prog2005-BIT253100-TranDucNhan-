for i in range(3):
    name = input("Nhập tên sinh viên: ")
    math_score = float(input("Điểm Toán: "))
    physics_score = float(input("Điểm Lý: "))
    chemistry_score = float(input("Điểm Hóa: "))

    average = (math_score + physics_score + chemistry_score) / 3
    print("Sinh viên:", name)
    print("Điểm trung bình:", round(average, 2))
    print("-------------------")
