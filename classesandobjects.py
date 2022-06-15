class Computer:

    def config(self):  # Method
        print("i5, 16g, 1TB")


comp1 = Computer()  # Instanciation/Object creation
comp2 = Computer()  # Constructor
print(type(comp1))

# Calling Method and passing Object as an argument to the method
Computer.config(comp1)
Computer.config(comp2)

# Another method to do the above (More commonly used)
comp1.config()
comp2.config()
