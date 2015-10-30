from random import randint

number = randint(0,100)
#print (number)
name = input("What is your name? ")
print ("Okay, " + str(name) + ", let's do this!")

for turn in range(50):

    guess = int(input("Guess the Number between 0 and 100: "))

    if number > 100 or number < 0:
        print ("That number is out of range!")
    else:
        if number == guess:
            print ("")
            print ("Congratulations," + str(name) + ", you have guessed the number")
            print ("")
            print ("It took you " + str(turn + 1) + " turns to guess it.")
            print ("The number was " + str(number) + ".")
            print ("")
            input("Press Enter to exit...")
            exit()
        elif number <= guess:
            print ("Lower")
        elif number >= guess:
            print ("Higher")
        else:
            print ("You done goofed")
