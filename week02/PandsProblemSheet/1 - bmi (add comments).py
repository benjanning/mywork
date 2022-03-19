# calculate a person's BMI
# author: Ben Janning



from unittest import result


height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

#formatting the result to 2 decimal places using the round function
round: BMI = round(BMI, 2)

print (f"Your BMI is {round}")

