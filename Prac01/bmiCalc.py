print("Body-mass-index calculator, by ALex")

weight = float(input("Please enter your weight in kgs:"))
height = float(input("Please enter your height in m"))

bmi = weight / height ** 2

print("Therefore your BMI value is:", bmi)
print("thank you!")