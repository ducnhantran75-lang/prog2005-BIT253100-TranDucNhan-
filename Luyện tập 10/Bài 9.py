class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._name = name
        self._age = age

    # getter
    def get_age(self):
        return self._age

    # setter
    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._age = age

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}"

    def speak(self):
        return "Hello!"

    @classmethod
    def create_default(cls):
        return cls("Unknown", 0)

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __eq__(self, other):
        return self._age == other._age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        if grade < 0:
            raise ValueError("Điểm không hợp lệ")
        self._grade = grade

    def __str__(self):
        return super().__str__() + f", Grade: {self._grade}"


# test
p = Person("A", 20)
s = Student("B", 18, 9)

print(p)
print(s)
print(p.speak())
print(Person.is_adult(20))
print(p == Person("C", 20))