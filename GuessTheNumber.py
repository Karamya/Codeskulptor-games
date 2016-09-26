# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# helper function to start and restart the game
num_range = 100 

def new_game():
    # initialize global variables used in your code here
    global secret_number
    global num_range
    global no_of_remaining_guess
    secret_number = random.randint(0, num_range)
    print "New game. Range is from 0 to %d" %num_range
    if num_range == 100:
        #print "Range is from 0 to 100"
        no_of_remaining_guess = int(math.ceil(math.log(100, 2)))
        print "Number of remaining guesses is %d" %no_of_remaining_guess
        print""
    else:
        #print "Range is from 0 to 1000"
        no_of_remaining_guess = int(math.ceil(math.log(1000, 2)))
        print "Number of remaining guesses is %d" %no_of_remaining_guess
        print""
    return


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    # remove this when you add your code    
    return

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    return
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    global secret_number
    global num_range
    global no_of_remaining_guess
    no_of_remaining_guess -= 1 
    if no_of_remaining_guess < 0:
        print "You ran out of guesses.  The number was %d" %secret_number
        print""
        new_game()
        
    print "Guess was %d" %guess    
    if guess == secret_number:
        print "Number of remaining guesses is %d" %no_of_remaining_guess
        print "Correct!"
        print""
    elif guess > secret_number:
        print "Number of remaining guesses is %d" %no_of_remaining_guess
        print "Lower!"
        print""
    else:
        print "Number of remaining guesses is %d" %no_of_remaining_guess
        print "Higher!"
        print""
        
        
    
    # remove this when you add your code
    
    
    return guess

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_input("Input Guess", input_guess,100)
frame.add_button("Range 100", range100)
frame.add_button("Range 1000", range1000)

# register event handlers for control elements and start frame

frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
