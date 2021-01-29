#Binary into hex

while(True):
    denaryNumber = int(input("Input a denary number: "))
    binaryNumber = bin(denaryNumber)
    hexNumber = hex(denaryNumber)

    print("Denary: " + str(denaryNumber) + "\n" + "Binary: " + str(binaryNumber) + "\n" + "Hex: " + str(hexNumber))

    raw_input("Press enter to loop again")
    print("")
