#BMI Calculator
#Niall Mc Donnell
#01/02/21

print("-------------------------------------------")
print("Body Mass Index Calculator")
print("-------------------------------------------")

weight = float(input("Please Enter your Weight "))
height = float(input("Please Enter your Height "))
BMI = weight / (height*height)

print(round (BMI,2))
if BMI < 19.00:
    print("You are Underweight")
elif BMI < 24.00:
    print("You are Healthy")
elif BMI < 30.00:
    print("You are Obese")
else:
    print("Extremly Overweight")
