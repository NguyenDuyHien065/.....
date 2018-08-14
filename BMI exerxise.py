mass = float(input(" Enter your mass(kg) :  "))
height = float(input(" Enter your height(m) :"))
bmi = mass / (height * height)
print (" Your BMI :  ",bmi)
if bmi < 16 :
    print("Severely underweight")
elif  16 < bmi < 18.5 :
    print("Underweight")
elif 18.5 < bmi < 25 :
    print ("Normal")
elif 25 < bmi < 30 :
    print ("Overweight")
else :
    print ("Obese")