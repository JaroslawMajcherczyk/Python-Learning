class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing")

class Mause(Animal):
   def speak(self):
        print(f"{self.name} is squeaking")

dog = Dog("Czarnuch")
cat = Cat("Puszek")
mause = Mause("Szczurzysko")

dog.eat()
dog.sleep()
dog.speak()
print()
cat.eat()
cat.sleep()
cat.speak()
print()
mause.eat()
mause.sleep()
mause.speak()
