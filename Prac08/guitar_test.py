from guitar import Guitar

test = Guitar("test", 1992, 100)
print(test)
test.get_age()
print(test.is_vintage())

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1992, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

for i, guitar in enumerate(guitars):
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost))