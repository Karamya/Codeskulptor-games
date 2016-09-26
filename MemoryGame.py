# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global list_of_cards, exposed, state, choice1, choice2, turns
    state = 0
    turns = 0
    choice1 = 0
    choice2 = 0
    list_of_cards = range(8)
    list_of_cards.extend(list_of_cards)
    random.shuffle(list_of_cards)
    exposed = [False for i in range(16)]
    print list_of_cards
    #print exposed


     
# define event handlers
def mouseclick(pos):
    global state, choice1, choice2, turns
    index = pos[0]//50
    if state == 0:
        if not exposed[index]:
            if list_of_cards[choice1]!=list_of_cards[choice2]:
                exposed[choice1] = False
                exposed[choice2] = False
            exposed[index]= True
            state = 1
            choice1 = index
    elif state == 1:
        if not exposed[index]:
            state = 0
            exposed[index] = True
            choice2 = index
            turns += 1
            label.set_text("Turns ="+str(turns))
        
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(list_of_cards)):
        canvas.draw_polygon([(i*50,0),((i+1)*50,0),((i+1)*50,100), (i*50,100)],3, "Green","Gray")
    for i in range(len(list_of_cards)):
        if exposed[i]:
            canvas.draw_polygon([(i*50,0),((i+1)*50,0),((i+1)*50,100), (i*50,100)],3, "Black","Green")
            canvas.draw_text(str(list_of_cards[i]), [i*50+10, 70], 60, "Black")
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



# Always remember to review the grading rubric
