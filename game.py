# Put your code here
import random


print "Hi player!"
name = raw_input("What is your name? ")
game_try = raw_input("Do you want to play a game? Enter Y for Yes or hit any other key for No. ")
# this is the lowest number of guesses made to reach correct number 
high_score = None

#this while loop controls if someone wants to play the game.
while game_try == "Y":
    number = random.randint(1, 100)
# print number
    guess = None
# print guess
    # this list keeps track of guesses made during one game 
    current_score = []
    
    # this while loop is the main game
    while guess != number:
        guess = raw_input("%s please choose a number between 1 and 100. " % (name))
        current_score.append(guess) # append guesses to an empty list to count later
        # print high_score


        #validates if the input is a digit
        if guess.isdigit():
            guess = int(guess)
            if guess >= 1 and guess <= 100:
                if guess < number:
                    print "%i was too low." % (guess)
                elif guess > number:
                    print "%i was too high." % (guess)
                else: 
                    print "Good job, %s! %i was the number." % (name, guess)
                    print "It took you %i guesses." % (len(current_score))
                    # compare high score to current score, tells user if they have high score
                    if high_score == None:
                        high_score = len(current_score)
                    else:
                        if high_score > len(current_score):
                            high_score = len(current_score)
                    print "The current high score is %i." % (high_score)
                    # asks player whether they want to play again and go through the main loop
                    
                    game_try = raw_input("Would you like to play again? Enter Y for Yes or any other key to exit. ")
            else:
                print "Please choose a number between 1 and 100."
        # if it's not a number, tells them 
        else:
            print "Hey %s, %s is not a number." % (name, guess) 
print "Okay maybe another time."
