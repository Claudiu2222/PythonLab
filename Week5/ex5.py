
class Animal:
    def __init__(self, name,age,weight):
        self.name = name
        self.age = age
        self.weight=weight

    def eat(self):
        print(self.name + " is eating")
    
    def sleep(self):
        print(self.name + " is sleeping")
    
    

class Fish(Animal):
    def __init__(self, name, water_type,age,weight):
        super().__init__(name,age,weight)
        self.water_type = water_type
        self.is_swimming = False

    
    def swim(self):
        print(self.name + " is swimming")
        self.is_swimming = True
    def stop_swimming(self):
        print(self.name + " stopped swimming")
        self.is_swimming = False
    def lay_eggs(self):
        print(self.name + " is laying eggs")

class Mammal(Animal):
    def __init__(self, name, fur_color, is_pregnant,age,weight):
        super().__init__(name,age,weight)
        self.fur_color = fur_color
        self.is_pregnant = is_pregnant
        self.has_offsprings = False
    def give_birth(self):
        if self.is_pregnant:
            print(self.name + " is giving birth")
            self.is_pregnant = False
            self.has_offsprings = True
        else:
            print(self.name + " is not pregnant")
    def feed_offspring(self):
        if self.has_offsprings:
            print(self.name + " is feeding its offsprings")
        else:
            print(self.name + " has no offspring")

class Bird(Animal):
    def __init__(self, name, wingspan,age,weight):
        super().__init__(name,age,weight)
        self.wingspan = wingspan
        self.is_flying = False
    def fly(self):
        print(self.name + " is flying")
        self.is_flying = True
    def stop_flying(self):
        print(self.name + " took a break from flying")
        self.is_flying = False
    def lay_eggs(self):
        if self.is_flying:
            print("Cannot lay eggs while flying")
        else:
            print(self.name + " is laying eggs")

fish1 = Fish("Nemo", "saltwater", 1, 0.5)
fish1.eat()
fish1.sleep()
fish1.swim()
fish1.lay_eggs()

mammal1 = Mammal("Simba", "golden", True, 2, 100)
mammal1.eat()
mammal1.give_birth()
mammal1.feed_offspring()

bird1 = Bird("Tweety", 20, 1, 0.1)
bird1.fly()
bird1.stop_flying()
bird1.lay_eggs()
