""" Summer Olympics
"""

for i in range(1992, 2017, 4):
    print(i)


""" Olympic cities """

olympic_cities = {1992: "Barcelona, Spain", 1996: "Atlanta, United States", 2000: "Sydney, Australia", 2004: "Athens, Greece", 2008: "Beijing, China", 2012: "London, United Kingdom", 2016: "Rio de Janeiro, Brazil"}

print("Welcome homedog, please choose an olympic year to see what city it was hosted in.")
print("It must be from 1992 - 2016")
choice = int(input(">>>"))
if choice in olympic_cities:
    print("In this year, the city chosen was", olympic_cities[choice])
else:
    print("Not a valid olympic year.")


""" """


""" Given the existing dictionary:
ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

Write code to prompt the user for a name and age, add these to the dictionary, then display all of the data nicely. Sample:

Name: Mario
Age: 34
Jack		-	 56
Bill 	-	 21
Mario 	-	 34
Jane 	-	 34
"""

ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

