
students = {
    "A": 7,
    "B": 7,
    "C": 6
}

def tinh_trung_binh(ds):
    tong = sum(ds.values())
    return tong / len(ds)


print("Điểm trung bình:", tinh_trung_binh(students))