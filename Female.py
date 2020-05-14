from Person import Person
import math

class Female(Person):

    def __init__(self, myName, surname, age, height, hip, neck, waist, weight):
        super().__init__(myName, surname, age, height, neck, waist, weight)
        self.hip = hip

    @property
    def katchMcArdle(self):
        return round(370 + (21.6 * self.leanMass), 2)

    @property
    def mifflinAndStJeor(self):
        return round((10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161, 2)

    @property
    def body_fat_percentage(self):
        return round(495 / (1.29579 - 0.35004 * (math.log10(self.waist + self.hip - self.neck)) + 0.221 * (math.log10(self.height))) - 450)
        
    def tdee(self, formula, activityFactor):
        return round(formula * activityFactor, 2)