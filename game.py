# Put your code here
import random


print "Hi player!"
name = raw_input("What is your name? ")

number = random.randint(1, 100)
# print number
guess = 0
# print guess
while guess != number:
    guess = raw_input("%s please choose a number between 1 and 100. " % (name))
    if guess.isdigit():
        guess = int(guess)
        if guess >= 1 and guess <= 100:
            if guess < number:
                print "That was too low."
            elif guess > number:
                print "That was too high."
            else: 
                print "Good job, %s! %i was the number." % (name, guess)
        else:
            print "Please choose a number between 1 and 100."
    else:
        print "Hey %s, %s is not a number." % (name, guess)
       
