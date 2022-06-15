class Student:

    def __init__(self, name, rollno) -> None:
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  # Object of inner class inside the outer class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:  # Class inside a class
        # Object of this inner class should be outside inner class

        def __init__(self) -> None:
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Alpha", 1)
s2 = Student("Beta", 2)

s1.show()
s2.show()

lap1 = s1.lap
lap2 = s2.lap


print(id(lap1), id(lap2))
