from random import randint

number = randint(0,100)
guess = int(raw_input("Guess the Number between 0 and 100:"))

if number > 100 or number < 0:
    print "That number is out of range!"

if number == guess:
    print "Congratulations, you have guessed The Number"
    print "The number was" number
elif number <= guess:
    print "Higher"
elif number >= guess:
    print "Lower"
else:
    print "You done goofed"
