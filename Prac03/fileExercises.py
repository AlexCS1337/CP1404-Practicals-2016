# Quick Program 1
outFile = open("name.txt", "w")
name = input("What is your name? ")
print("Your name is", name)
outFile.close()

# Quick Program 2
inFile = open("name.txt", "r")
name = inFile.read().strip()
print("Your name is", name)
inFile.close()

# Quick Program 3
inFile = open("numbers.txt", "r")
number1 = int(inFile.readline())
number2 = int(inFile.readline())
print(number1 + number2)
inFile.close()

# Quick Program 3 extended
inFile = open("numbers.txt", "r")
total = 0
for line in inFile:
    number = int(line)
    total += number
print(total)
inFile.close()