class Student:

    school = "ABC"

    def __init__(self, m1, m2, m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # Instance method
        return ((self.m1+self.m2+self.m3)/3)

    def get_m1(self):  # Getters / Accessor method
        return self.m1

    def set_m1(self, value):  # Seters / Mutator method
        self.m1 = value

    @classmethod  # Decorator
    def get_School(cls):  # Class method
        return cls.school

    @staticmethod
    def info():  # Static method
        print("This is Student CLass.. in some module")


s1 = Student(34, 36, 39)
s2 = Student(36, 38, 40)

print(s1.avg())
print(s2.avg())
print(Student.get_School())
