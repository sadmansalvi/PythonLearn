#not rewriting a def inside a class
class Mammal:
    def walk(self):
        print("walk")


#inherited change from mammal
class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass #make python happy and tell to pass


dog1 = Dog()
dog1.walk()
dog1.bark()