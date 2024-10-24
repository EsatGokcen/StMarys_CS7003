answer = []
loop = True

while loop == True:

    option = input("What calculation would you like to perform?\n-Add\n-Substract\n-Multiply\n-Divide\nPlease type your option here: ")

    value1 = float(input("\n\nEnter first value to calculator: "))
    value2 = float(input("\nEnter second value to calculator: "))

    if option == "Add":
        answer = value1 + value2
        print(answer)
    elif option == "Substract":
        answer = value1 - value2
        print(answer)
    elif option == "Multiply":
        answer = value1 * value2
        print(answer)
    elif option == "Divide":
        answer = value1 / value2
        print(answer)
    else:
        restart2 = input("Invalid option please type 'y' to restart or 'n' to stop: ")
        
        if restart2 == "y":
            print("\n\nRestarting...\n\n")
        elif restart2 == "n":
            print("\n\nOk, goodbye.\n\n")
            loop = False
        else:
            print("\n\nLearn to type...\n\n")

    restart = input("\nWould you like to go again?: (y)/(n) ")
    if restart == "y":
            print("\n\nRestarting...\n\n")
    elif restart == "n":
        print("\n\nOk, goodbye.\n\n")
        loop = False
    else:
        print("\n\nLearn to type...\n\n")


    

    
    

