from operator import truediv


class Computer:

    # Self points to current object inside a class
    def __init__(self) -> None:
        self.name = "Alpha"
        self.code = 12345

    def update(self):
        self.code = 54321

    def compare(self, other):
        if self.name == other.name:
            return True


c1 = Computer()  # Constructor
c2 = Computer()

print(id(c1))  # Prints address of object
print(id(c2))

if c1.compare(c2):  # Making our own function
    print("Names are same")

if c2.compare(c1):
    print("Names are same")

c1.name = "Beta"  # Passing our own data
c2.update()

print(c1.name, c1.code)
print(c2.name, c2.code)
