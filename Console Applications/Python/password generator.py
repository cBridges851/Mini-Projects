# -*- coding: cp1252 -*-
#                         Password Generator

##Objectives
#Choose the length of the password
#Include a combination of letters (upper and lower case), numbers and symbols

#Ask for length of password

# -*- coding: cp1252 -*-

import random

print("--Welcome to Pa$$w0rd G3n3rat0r!--")

def AskForLengthOfPassword():
    lengthOfPassword = int(input("How many characters would you like your password to have?"))#Ask for number of characters the password should have

    if lengthOfPassword < 6:
        print("Your password is too short \n")
        AskForLengthOfPassword() #If the password is to be fewer than 6 characters, the user is told that the length is too short and they are asked for the length again

    else:
        GeneratePassword(lengthOfPassword); #If the password is 6 characters or above, the function that generates the function is called

def GeneratePassword(lengthOfPassword):
    lowerCaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperCaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '"', '£', '$', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', "'", '@', '~', '#', ',', '.', '<','>','?','/']
    allCharacters = [lowerCaseLetters, upperCaseLetters, numbers, symbols] #Characters that can be selected

    password = "" #Empty string that will be added to upon input.
    
    for i in range(0, lengthOfPassword):
        randomCategory = random.randint(0,3) #Random number generated to select array

        if randomCategory == 0:
            randomNumber = random.randint(0, len(lowerCaseLetters)-1)
            randomCharacter = lowerCaseLetters[randomNumber]
            password = password + randomCharacter

        elif randomCategory == 1:
            randomNumber = random.randint(0, len(upperCaseLetters)-1)
            randomCharacter = upperCaseLetters[randomNumber]
            password = password + randomCharacter

        elif randomCategory == 2:
            randomNumber = random.randint(0, len(numbers)-1)
            randomCharacter = numbers[randomNumber]
            password = password + randomCharacter

        else:
            randomNumber = random.randint(0, len(symbols)-1)
            randomCharacter = symbols[randomNumber]
            password = password + randomCharacter

    print("Here is your randomly generated password: " + password)#Outputs the password
    NewPassword() #Calls the function that asks the user if they want to generate another password

def NewPassword():
    newQuestion = input("Would you like to generate another password (y/n)?")

    if newQuestion == 'y' or newQuestion == 'Y' or newQuestion == "yes" or newQuestion == 'YES' or newQuestion == "Yes":
        print("")
        AskForLengthOfPassword() #Calls the function that asks for the length of password

    elif newQuestion == 'n' or newQuestion == 'N' or newQuestion == "no" or newQuestion == "NO" or newQuestion == "No":
        quit() #Terminates the program

    else:
        print("Invalid input")
        NewPassword() #Asks again

AskForLengthOfPassword()
