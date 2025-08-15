class Animal:
    def __init__(self, na):
        self.name = na
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}The dog barks")


d1 = Dog("Buddy")
d1.speak()