from Female import Female
from Male import Male

while True:
    print()

    print("Male   -> x\nFemale -> y")

    gender = input("Gender: ")

    fname = "William"  # input('First name: ')
    lname = "Lopes"  # input('Last name: ')
    age = 33  # int(input('Age: '))
    height = 168  # int(input('Height (in centimeters): '))
    neck = 37  # float(input('Neck size (in centimeters): '))
    waist = 87  # float(input('Waist size (in centimeters): '))
    weight = 65  # float(input('Weight (in Kilograms): '))s

    '''
    fname = input('First name: ')
    lname = input('Last name: ')
    age = int(input('Age: '))
    height = int(input('Height (in centimeters): '))
    neck = float(input('Neck size (in centimeters): '))
    waist = float(input('Waist size (in centimeters): '))
    weight = float(input('Weight (in Kilograms): '))
    '''

    if gender == 'y':
        hip = float(input("Hip size(in centimeters): "))
        obj = Female(fname, lname, age, height, hip, neck, waist, weight)
    elif gender == 'x':
        obj = Male(fname, lname, age, height, neck, waist, weight)
    else:
        print("Insert a valid option")

    # obj = Male('william', 'lopes', 33, 168, 37.5, 86.5, 68)

    print("- Choose the Formula -\nKatch McArdle -> 1\nMifflin and St Jeor -> 2")
    formula = int(input("Enter your choice: "))

    print()
    print("- Choose your level of exercise -")
    print("Little/no exercise ------------------------------------------- a")
    print("Light exercise ( 1-3 days per week ) ------------------------- b")
    print("Moderate exercise ( 3-5 days per week ) ---------------------- c")
    print("Heavy exercise ( 6-7 days per week ) ------------------------- d")
    print("Very heavy exercise ( twice per day, extra heavy workouts ) -- e")

    activityFactor = input("Enter your exercise level: ")

    if activityFactor   == "a": activityFactor = 1.2
    elif activityFactor == "b": activityFactor = 1.375
    elif activityFactor == "c": activityFactor = 1.55
    elif activityFactor == "d": activityFactor = 1.725
    elif activityFactor == "e": activityFactor = 1.9
    else: print("option not valid")

    print()
    if formula == 1:
        print("bmr = " + str(obj.katchMcArdle) + " calories")
        tdee = obj.tdee(obj.katchMcArdle, activityFactor)
        print(
            "TDEE (Katch-McArdle) = "
            + str(tdee)
            + " calories"
        )
    else:
        print("bmr = " + str(obj.mifflinAndStJeor) + " calories")
        tdee = obj.tdee(obj.mifflinAndStJeor, activityFactor)
        print(
            "TDEE (Mifflin St Jeor) = "
            + str(obj.tdee(obj.mifflinAndStJeor, activityFactor))
            + " calories"
        )

    print("BF (Body Fat)  = " + str(obj.body_fat_percentage) + " %")
    print("FM (Fat Mass)  = " + str(obj.fatMass) + " kg")
    print("LM (Lean Mass) = " + str(obj.leanMass) + " kg")

    print()
    print('- Objetivo -')
    print('Lose Weight - a\nGain Weight - b')
    goal = input('Enter: ')

    print()
    print('How much per day?\n10% - a\n20% - b\n30% - c')
    percentage = input('Enter: ')

    # Lose weight (cant be less than 1200 if woman or 1800 man)
    if goal == 'a':
        if percentage == 'a':
            calories = tdee - tdee * 0.1
            if gender == 'x' and calories < 1800:
                calories = 1800
                print('Daily calories to achieve your goal is: ' + str(calories) + ' calories' )
            elif gender == 'y' and calories < 1200:
                calories = 1200
                print('Daily calories to achieve your goal is: ' + str(calories) + ' calories')

        if percentage == 'b':
            calories = tdee - tdee * 0.2
            if gender == 'x' and calories < 1800:
                calories = 1800
                print('Daily calories to achieve your goal is: ' + str(calories) + ' calories')
            elif gender == 'y' and calories < 1200:
                calories = 1200
                print('Daily calories to achieve your goal is: ' + str(calories) + ' calories')

        if percentage == 'c':
            calories = tdee - tdee * 0.3
            if gender == 'x' and calories < 1800:
                calories = 1800
                print('Daily calories to achieve your goal is: ' + str(calories) + ' calories')
            elif gender == 'y' and calories < 1200:
                calories = 1200
                print('Daily calories to achieve your goal is: ' + str(calories) + ' calories')

    elif goal == 'b':
        if percentage == 'a':
            calories = tdee * 0.1 + tdee
            print('Daily calories to achieve your goal is: ' + str(calories) + ' calories')
        if percentage == 'b':
            calories = tdee * 0.2 + tdee
            print('Daily calories to achieve your goal is: ' + str(calories) + ' calories')
        if percentage == 'c':
            calories = tdee * 0.3 + tdee
            print('Daily calories to achieve your goal is: ' + str(calories) + ' calories')

    # Gain weight
