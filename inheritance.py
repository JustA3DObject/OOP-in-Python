class A:

    def __init__(self) -> None:
        print("in A init")

    def method1(self):
        print("1")

    def method2(self):
        print("2")


class B(A):

    def __init__(self) -> None:
        super().__init__()
        print("in B init")

    def method3(self):
        print("3")

    def method4(self):
        print("4")


class C():

    def __init__(self) -> None:
        print("in C init")

    def method5(self):
        print("5")


class D(B, C):

    def __init__(self) -> None:
        super().__init__()

    def method6(self):
        print("6")


a1 = A()
a1.method1()
a1.method2()

b1 = B()
b1.method1()
b1.method2()
b1.method3()
b1.method4()

c1 = C()
c1.method5()

d1 = D()
d1.method1()
d1.method2()
d1.method3()
d1.method4()
d1.method5()
d1.method6()
