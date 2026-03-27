students = {
    "An": 8,
    "Bình": 7,
    "Cường": 9
}

def avg_score(d):
    return sum(d.values()) / len(d)

print("Điểm trung bình:", avg_score(students))