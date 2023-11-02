class Animal:
    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size

    def talk(self):
        print("Mmmmmmm...")

    def eat(self, meal):
        self.size += len(meal)
        self.weight += len(meal)


class Herbivore(Animal):
    def __init__(self, name, weight, size, ratio):
        super().__init__(name, weight, size)
        self.ratio = ratio

    def eat(self, meal):
        if meal in self.ratio:
            super().eat(meal)


class Predator(Animal):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)
        self.prey_eaten = set()

    def eat(self, meal):
        if meal not in self.prey_eaten and self.size > len(meal):
            self.prey_eaten.add(meal)
            increase = len(meal) * 0.2
            self.size += increase
            self.weight += increase


class Goose(Herbivore):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size, ["grass"])
        self.sound = "Honk"

    def talk(self):
        print(f"{self.name} says {self.sound}")

    def fly(self):
        print(f"{self.name} is flying!")


class Wolf(Predator):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)
        self.sound = "Howl"

    def talk(self):
        print(f"{self.name} says {self.sound}")

    def hunt(self, prey):
        print(f"{self.name} is hunting {prey}!")


goose1 = Goose("Goose 1", 10, 20)
goose2 = Goose("Goose 2", 8, 18)
wolf1 = Wolf("Wolf 1", 30, 40)
wolf2 = Wolf("Wolf 2", 25, 35)

goose1.talk()
goose1.eat("grass")
goose1.eat("meat")
goose1.fly()

wolf1.talk()
wolf1.hunt("Goose 1")
wolf1.eat("Goose 1")
wolf1.eat("Goose 1")
wolf1.hunt("Goose 2")
wolf1.eat("Goose 2")
