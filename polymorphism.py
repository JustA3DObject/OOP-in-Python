# Python does not have method overloading by default

a = 5
b = 6
print(a+b)
print(int.__add__(a, b))  # + calls __add__ under the hood


class Student:

    def __init__(self, m1, m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # Operator overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = Student(m1, m2)

        return m3

    def sum(self, a=None, b=None, c=None):  # Method overloading manually
        if a != None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        else:
            s = a
        return s


s1 = Student(9, 7)
s2 = Student(10, 5)

s3 = s1+s2
print(s3.m1)

print(s1.sum(9, 7))
print(s1.sum(9, 7, 10))

# Method Overriding


class A:

    def show(self):
        print("in A show")


class B(A):

    def show(self):
        print("in B show")


a1 = A()
a1.show()

a2 = B()
a2.show()
