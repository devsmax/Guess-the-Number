from random import randint

number = randint(0,100)
guess = int(raw_input("Guess the Number between 0 and 100:"))

if number > 100 or number < 0:
    print "That number is out of range!"
