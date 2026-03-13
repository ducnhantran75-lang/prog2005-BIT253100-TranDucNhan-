class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")

s = Student("A", 10)
s.display()
