from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, myName, surname, age, height, neck, waist, weight):
        self.myName = myName
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.neck = neck
        self.waist = waist
    
    @abstractmethod
    def body_fat_percentage(self):
        pass
    
    @property
    def fatMass(self):
        return round(self.body_fat_percentage / 100 * self.weight, 2)
    
    @property
    def leanMass(self):
        return round(self.weight - self.fatMass, 2)
    
    @abstractmethod
    def tdee(self, bmr, activityFactor):
        pass
    
    def gain(self):
        pass

    def lose(self):
        pass
            
    def __repr__(self):
        return f"{self.myName}, {self.surname}, {self.age}, {self.height}, {self.weight}, {self.neck}, {self.waist}"

    def __str__(self):
        return f"{self.myName} {self.surname}"
