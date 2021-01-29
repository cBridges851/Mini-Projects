#Hex Colours
while True:
    print("***Hex Colour Caluculator***")
    red = int(input("Enter the value of red in the colour: "))
    green = int(input("Enter the value of green in the colour: "))
    blue = int(input("Enter the value of blue in the colour: "))

    redHex = hex(red)
    greenHex = hex(green)
    blueHex = hex(blue)

    print(redHex + "|" + greenHex + "|" + blueHex)
    print(" ")
