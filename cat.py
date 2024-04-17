class Cat:
    name = None
    age = None
    __isHappy : None

    # constructor
    def __init__(self, name, age, isHappy = True):
        self.name = name,
        self.age = age,
        self.__isHappy = isHappy

    def sound(self):
        print("Weow")

    def display(self):
        print("Happy", self.__isHappy)

    # getter
    def get_isHappy(self):
        return self._isHappy
    
    # setter 
    def set_isHappy(self, new_happy):
        self._isHappy = new_happy

# child class
class DomesticCat(Cat):
    owner = None

    def __init__(self, owner, name, age, isHappy = True):
        super().__init__(name, age, isHappy)
        self.owner = owner

class WildCat(Cat):
    def sound(self):
        print("Hiss")

# create instance
Cat1 = Cat("Meo Meo", 3)
print(Cat1.sound())

Cat2 = DomesticCat("Mikhir", "Kitkat", 2)
print(Cat2.owner)

Cat3 = WildCat("abc", "efg", 3)
print(Cat3.sounnd)