class Student:
    def __init__(self, name, score):
        if 0<= score <= 10:
            self.score = score
        else:
            raise ValueError("Diem phai tu 0 den 10")
        self.name = name
