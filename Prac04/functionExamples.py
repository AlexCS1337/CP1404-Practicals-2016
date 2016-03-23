def calcAreaRectangle(length, width):
    return length * width

def convert_celsius_fahrenheit(celsius):
    return celsius * 1.8 + 32.00

def calcBodyMassIndex(height, weight):
    return weight / height ** 2

print("This is a test", calcAreaRectangle(10, 10))
print("Fahrenheit =", convert_celsius_fahrenheit(10))