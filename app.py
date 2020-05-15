from Male import Male
from Female import Female

# 1 == Male
# 2 == Female

print('Male -> 1')
print('Female -> 2')
sex = int(input('Sex: '))
    
firstName = input('First name: ')
lastName = input('Last name: ')
age = int(input('Age: '))
height = int(input('Height (in centimeters): '))
neck = float(input('Neck size (in centimeters): '))
waist = float(input('Waist size (in centimeters): '))
weight = float(input('Weight (in Kilograms): '))

if sex == 2:
    hip = float(input('Hip size(in centimeters): '))
    obj = Female(firstName, lastName, age, height, hip, neck, waist, weight)
elif sex == 1:
    obj = Male(firstName, lastName, age, height, neck, waist, weight)
else:
    print('Insert a valid option')

# obj = Male('william', 'lopes', 33, 168, 37.5, 86.5, 68)

print('- Choose the Formula -\n Katch McArdle -> 1\n Mifflin and St Jeor -> 2')
formula = int(input('Enter your choice: '))

print()
print('- Choose your level of exercise -')
print('Little/no exercise	- 		                                - 1.2')
print('Light exercise		- 1-3 days per week			            - 1.375')
print('Moderate exercise	- 3-5 days per week			            - 1.55')
print('Heavy exercise		- 6-7 days per week			            - 1.725')
print('Very heavy exercise	- twice per day, extra heavy workouts   - 1.9')

activityFactor = float(input('Enter your exercise level: '))

print()
if formula == 1:
    print('bmr = ' + str(obj.katchMcArdle) + ' calories')
    print('TDEE (Katch-McArdle) = ' + str(obj.tdee(obj.katchMcArdle, activityFactor)) + ' calories')
else:
    print('bmr = ' + str(obj.mifflinAndStJeor) + ' calories')
    print('TDEE (Mifflin St Jeor) = ' +
          str(obj.tdee(obj.mifflinAndStJeor, activityFactor)) + ' calories')

print('bf = ' + str(obj.body_fat_percentage) + ' %')
print('fat mass = ' + str(obj.fatMass) + ' kg')
print('lean mass = ' + str(obj.leanMass) + ' kg')


