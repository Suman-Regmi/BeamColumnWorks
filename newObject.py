class Animal:
    def __init__(self, type):
        self.type = type
        
    # that means there is a direct access of the super functions into the child classes
    def makeASound(self):    
        print(self.sound)


class Horse(Animal):
    def __init__(self,name):
        super().__init__("Horse")
        self.name = name
        self.sound = "Mohahah"


class Dog(Animal):
    def __init__(self,name):
        super().__init__("Dog")
        self.name = name
        self.sound = "HowHow"


myHorse = Horse("Jack")
myHorse.makeASound()


