# fatMass = bodyFat * weight in kg / 100
# leanMass = fatWeight - bodyWeight

# Recommended daily calorie intake to maintain current weight.
# Daily Calories = EXERCISE_LEVEL_FACTOR * BMR

'''
Harris-Benedict Principle: Use the following table to calculate your recommended daily calorie intake to maintain current weight.
Exercise Level		    Details	Calorie 			            Calculation (Daily Needs)
Little/no exercise	 					                        BMR x 1.2
Light exercise		    1-3 days per week			            BMR x 1.375
Moderate exercise	    3-5 days per week			            BMR x 1.55
Heavy exercise		    6-7 days per week			            BMR x 1.725
Very heavy exercise	    twice per day, extra heavy workouts	    BMR x 1.9
'''

# Army Body Fat Formula (Body Fat)
# Men BF = 495 / (1.0324 - 0.19077 * (log(waist_in_cm - neck_in_cm)) + 0.15456 * (log(height_in_cm))) - 450
# Women BF % = 495 / ( 1.29579 - 0.35004(log(waist+hip-neck)) + 0.22100(log(height))) - 450

'''
Basal metabolic rate(BMR) 
    is the amount of energy required to maintain the body's normal metabolic activity, such as respiration, maintenance of body temperature(thermogenesis), and digestion. Specifically, it is the amount of energy required at rest with no additional activity. The energy consumed is sufficient only for the functioning of the vital organs such as the heart, lungs, nervous system, kidneys, liver, intestine, sex organs, muscles, and skin.
'''
'''
Variance:
The resting and basal metabolic rate generally decrease with age or if there is a decline in lean body mass. Activities that tend to increase muscle mass (lean tissue) such as body building or strength training (anaerobic activities), will also increase the basal or resting metabolic rate. Aerobic activities such as running, skating, or rope jumping may improve endurance but have little effect on the basal or resting metabolic rate (see post-exercise expenditure). Other factors that may affect the BMR or RMR(BMR*Exercice Level Factor) include stress, illness, hormone levels (e.g. thyroid), environmental (e.g. temperature or altitude) or any other factor that effects the normal functioning of one or more vital organs.

Lean tissue requires significantly more energy to maintain because of the increased level of metabolic activity. In contrast, fat tissue requires very little energy to maintain and has little influence on the resting or basal metabolic energy needs.

Regular exercise increases the amount of energy you burn while you are exercising. But it also boosts your resting energy expenditure — the rate at which you burn calories when the workout is over and you are resting. Resting energy expenditure remains elevated as long as you exercise at least three days a week on a regular basis.
'''

# Harris–Benedict equations to calculate basal methabolic rate
# Men BMR = 66.5 + ( 13.75 × weight in kg ) + ( 5.003 × height in cm ) – ( 6.755 × age in years )
# Women	BMR = 655 + ( 9.563 × weight in kg ) + ( 1.850 × height in cm ) – ( 4.676 × age in years )

# The Harris–Benedict equations revised by Roza and Shizgal in 1984.[3]
# Men	BMR = 88.362 + (13.397 × weight in kg) + (4.799 × height in cm) - (5.677 × age in years)
# Women	BMR = 447.593 + (9.247 × weight in kg) + (3.098 × height in cm) - (4.330 × age in years)

# The Harris–Benedict equations revised by Mifflin and St Jeor in 1990: [4]
# Men	BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) + 5
# Women	BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) - 161

# The Katch-McArdle formula is used to predict Resting Daily Energy Expenditure (RDEE)
# P = 370 + (21.6 * l) -> where l is Lean Body Mass in Kgs

'''
Food is converted into energy for our body’s to function through the three energy-yielding nutrients, protein, lipids (fats), and carbohydrates. The percentage of each energy-yielding nutrient (macronutrient) that should be consumed daily as part of a healthy diet is:

45% to 65% of kcalories should come from carbohydrates
20% to 35% of kcalories should come from fats
10% to 35% of kcalories should come from protein
'''

'''
Although established around 100 years ago, we still use the Harris–Benedict prediction in the physical activity lab. Due to changes in lifestyle, new predictions such as the Mifflin St Jeor equation are more accurate. Working with obese patients (BMI 30 or more) the Broca-Index correction makes sense.
All these measurements simply rely on bodyweight, height, age and gender.
If you are able to measure lean body mass by bioelectrical impedance analysis you can predict the daily resting energy expenditure by Katch-McArdle and Cunningham formula, respectively.
Concerning you question, the difference between Harris–Benedict and Mifflin St Jeor equations is around 5%, with higher accuracy of the later one.
'''

'''
Women should not eat fewer than 1,200 calories a day, and men should not eat fewer than 1,800 calories a day, according to the American College of Sports Medicine. If subtracting 500 calories puts you below those numbers, you'll need to cut fewer calories from your diet and exercise more to burn the rest.
'''

'''
Total daily energy expenditure ( TDEE ) 
is a measurement of how many calories your body burns through during a standard day. It considers your BMR as well as the calories you burn during the activities and exercise you engage in on a daily basis. To compute your TDEE, you will need to indicate your average daily activity level.
'''

'''
“It takes 24-48 hours for the bulk of recovery to occur after a challenging workout, so it’s important on a rest day to consume enough carbohydrates to use as energy to recover, enough quality fats to bring inflammation down and support the heart and joints, and enough protein to repair body tissues,” she says.

You want to eat 20-30 grams of protein several times throughout the day, rather than eating very little at breakfast and 50 grams at dinner. This helps keep recovery constant, she explains.

“Many guys also assume they can cut back on protein on rest days, but in reality, the body continues to make protein almost 48 hours after a workout. Not eating enough protein or calories can hinder your muscle growth and athletic performance,” Rizzo explains

While your diet and nutrient ratio shouldn’t change much between rest and active days, your hunger levels might fluctuate. “Some research points to the fact that when someone participates in a high energy workout, their hunger levels are usually suppressed immediately after the workout, so they don’t take in as many calories as they are burning off,” Rizzo says.

You may feel hungrier on a rest day because your body is craving to get in those calories that it burned off the previous day. Or, maybe your appetite hormones are finally starting to return to normal, she explains.

“For example, during exercise, the blood moves to your muscles and away from the gut, which can cause you to eat less. The next day, the body will regulate itself with an increase in the hormone ghrelin (which makes us feel hungry) and a decrease in the hormone leptin (which makes us feel satiated,” says Rizzo.

But don’t pig out. To avoid mindlessly eating, make sure you eat plenty of protein, fiber, and healthy fats to keep you feeling full. You also want to stay hydrated on off-days, even if you’re not sweating or thirsty. “Staying adequately hydrated on your day off is essential for reaping the benefits from tomorrow’s workout,” she says.

Plus, inflammation can incur after a workout and continue into a rest day, so eat plenty of antioxidant-rich foods, like beets, berries, and leafy greens to decrease inflammation, she adds.
'''


from Person import Person
import math

class Male(Person):

    def __init__(self, myName, surname, age, height, neck, waist, weight):
        super().__init__(myName, surname, age, height, neck, waist, weight)
    
    @property
    def katchMcArdle(self):
        return round(370 + (21.6 * self.leanMass), 2)

    @property
    def mifflinAndStJeor(self):
        return round((10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5, 2)

    @property
    def body_fat_percentage(self):
        return round(495 / (1.0324 - 0.19077 * (math.log10(self.waist - self.neck)) + 0.15456 * (math.log10(self.height))) - 450, 2)

    def tdee(self, formula, activityFactor):
        return round(formula * activityFactor, 2)



