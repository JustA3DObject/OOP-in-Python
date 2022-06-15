class Car:

    wheels = 4

    def __init__(self) -> None:
        self.brand = "BMW"  # Instance variable
        self.mil = 10


c1 = Car()
c2 = Car()

c2.mil = 9  # Changing instance variable

print(c1.brand, c1.mil, c1.wheels)
print(c2.brand, c2.mil, c2.wheels)

Car.wheels = 5  # Changing Class/Static variable

print(c1.brand, c1.mil, c1.wheels)
print(c2.brand, c2.mil, c2.wheels)
