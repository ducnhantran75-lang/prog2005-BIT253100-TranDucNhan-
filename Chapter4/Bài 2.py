def diem_trung_binh(students):
    tong = sum(students.values())
    so_sv = len(students)
    return tong / so_sv

students ={
    "A": 7,
    "B": 8,
    "C": 9
}

avg = diem_trung_binh(students)

print("Diem trung binh:", avg)
