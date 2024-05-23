

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI <= 24.9:
    print("You have normal weight.")
elif 25 <= BMI <= 29.9:
    print("You are over weight.")
elif 30 <= BMI <= 34.9:
    print("You are obesity.")
elif 35 <= BMI <= 39.9:
    print("You are extreme obesity.")
else:
    print("You are severely obese.")