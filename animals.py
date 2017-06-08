class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

    def display(self):
        print self.health
        return self

dog1 = Animal("Dog", 150)
dog1.walk().walk().walk().run().run().display()

class Dog(Animal):
    
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    
    def pet(self):
        self.health += 10
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name, 170)
    
    def fly(self):
        self.health -= 10
        return self

dragon = Dragon("Cali")
dragon.fly().display()

# dog = Dog("Cali")
# dog.pet().display()