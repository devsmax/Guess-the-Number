from random import randint

number = randint(0,100)
#print (number)
for turn in range(50):

    guess = int(input("Guess the Number between 0 and 100:"))

    if number > 100 or number < 0:
        print ("That number is out of range!")
    else:
        if number == guess:
            print ("Congratulations, you have guessed The Number")
            print ("The number was " + str(number))
            input("Press Enter to exit...")
            exit()
        elif number <= guess:
            print ("Lower")
        elif number >= guess:
            print ("Higher")
        else:
            print ("You done goofed")
