class Computer:

    # init method doesn't need to be called and it'll execute for all the objects
    def __init__(self, cpu, ram):  # Three parameters accept object adn two values
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is: ", self.cpu, self.ram)


comp1 = Computer("i5", 16)
comp2 = Computer("Ryzen 3", 8)

comp1.config()
comp2.config()
