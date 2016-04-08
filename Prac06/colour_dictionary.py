COLOUR_CODES = {"Purple": "660066", "Cream Green": "9aff9a", "Cyan": "a0ffee", "Grey": "666666",
                "Green": "46a346", "Aqua": "008272", "Blue": "36aebc", "Pink": "f45cff"}
#print(COLOUR_CODES)

colour = input("Enter colour: ")
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Colour not found.")
    colour = input("Enter colour: ")