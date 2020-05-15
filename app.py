from Female import Female
from Male import Male

while True:
    print()
    # 1 == Male
    # 2 == Female

    print("Male -> 1")
    print("Female -> 2")
    sex = int(input("Sex: "))

    firstName = "William"  # input('First name: ')
    lastName = "Lopes"  # input('Last name: ')
    age = 33  # int(input('Age: '))
    height = 168  # int(input('Height (in centimeters): '))
    neck = 37  # float(input('Neck size (in centimeters): '))
    waist = 87  # float(input('Waist size (in centimeters): '))
    weight = 68  # float(input('Weight (in Kilograms): '))s

    if sex == 2:
        hip = float(input("Hip size(in centimeters): "))
        obj = Female(firstName, lastName, age,
                     height, hip, neck, waist, weight)
    elif sex == 1:
        obj = Male(firstName, lastName, age, height, neck, waist, weight)
    else:
        print("Insert a valid option")

    # obj = Male('william', 'lopes', 33, 168, 37.5, 86.5, 68)

    print("- Choose the Formula -\n Katch McArdle -> 1\n Mifflin and St Jeor -> 2")
    formula = int(input("Enter your choice: "))

    print()
    print("- Choose your level of exercise -")
    print("Little/no exercise                                           - a")
    print("Light exercise ( 1-3 days per week ) 			            - b")
    print("Moderate exercise ( 3-5 days per week )			            - c")
    print("Heavy exercise ( 6-7 days per week )		                    - d")
    print("Very heavy exercise ( twice per day, extra heavy workouts )  - e")

    activityFactor = input("Enter your exercise level: ")

    if activityFactor == "a":
        activityFactor = 1.2
    elif activityFactor == "b":
        activityFactor = 1.375
    elif activityFactor == "c":
        activityFactor = 1.55
    elif activityFactor == "d":
        activityFactor = 1.725
    elif activityFactor == "e":
        activityFactor = 1.9
    else:
        print("option not valid")

    print()
    if formula == 1:
        print("bmr = " + str(obj.katchMcArdle) + " calories")
        print(
            "TDEE (Katch-McArdle) = "
            + str(obj.tdee(obj.katchMcArdle, activityFactor))
            + " calories"
        )
    else:
        print("bmr = " + str(obj.mifflinAndStJeor) + " calories")
        print(
            "TDEE (Mifflin St Jeor) = "
            + str(obj.tdee(obj.mifflinAndStJeor, activityFactor))
            + " calories"
        )

    print("bf = " + str(obj.body_fat_percentage) + " %")
    print("fat mass = " + str(obj.fatMass) + " kg")
    print("lean mass = " + str(obj.leanMass) + " kg")
