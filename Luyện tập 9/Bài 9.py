class animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("animal sound")


class dog(animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Hoo Hoo")

d = dog("Siuuuu")
print(d.name)
d.sound()