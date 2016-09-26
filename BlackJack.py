# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    
happy = simplegui.load_image("http://www.avatarsdb.com/avatars/mowgli_happy_face.jpg")
sad = simplegui.load_image("http://images4.fanpop.com/image/polls/810000/810077_1313792547609_100.jpg?v=1313793002")
playing = simplegui.load_image("http://www.avatarsdb.com/avatars/mowgli_jungle_book.jpg")
bhappy = simplegui.load_image("http://v.dreamwidth.org/15792/9039")
bsad = simplegui.load_image("http://images4.fanpop.com/image/polls/652000/652949_1298951364658_100.jpg?v=1298951443")
# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        pass	# create Hand object

    def __str__(self):
        hand_string = "Hand contains "
        for card in self.hand:
            hand_string = hand_string + str(card)+" "
        return hand_string

    def add_card(self, card):
        self.hand.append(card)
        

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        aces = False
        
        for card in self.hand:
            if card.get_rank() == 'A':
                aces = True         
            hand_value = hand_value + VALUES.get(card.get_rank())
        if aces and hand_value + 10<= 21:
            return hand_value + 10
        else:
            return hand_value
            
        
   
    def draw(self, canvas, pos):
        for card in self.hand:
            card_loc = (CARD_SIZE[0] * (0.5 + RANKS.index(card.rank)), CARD_SIZE[1] * (0.5 + SUITS.index(card.suit)))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_SIZE[0] / 2 + self.hand.index(card)*CARD_SIZE[0], pos[1] + CARD_SIZE[1] / 2], CARD_SIZE)

        pass	# draw a hand on the canvas, use the draw method for cards
                       
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(str(suit),str(rank)))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.card = self.deck[-1]
        self.deck.remove(self.card)
        return self.card
        pass	# deal a card object from the deck
    
    def __str__(self):
        cards = "Deck contains "
        for card in self.deck:
            cards = cards + str(card) + " "
        return cards
        pass	# return a string representing the deck
        
#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, my_deck
    outcome = " "
    in_play = True
    player_hand = Hand()
    dealer_hand = Hand()
    my_deck = Deck()
    my_deck.shuffle()
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())

def hit():
    # replace with your code below
    global outcome, in_play, player_hand, dealer_hand, score
    if in_play:
        player_hand.add_card(my_deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = "You are busted. New Deal?"
            score -= 1 
            in_play = False
        elif in_play:
            outcome = " Hit or Stand"
       
def stand():
    # replace with your code below
    global score, outcome, in_play
    if in_play:
        if player_hand.get_value() > 21:
            outcome = "You are busted. New Deal?"
            score -= 1
            in_play = False
            return score, outcome, in_play
        else:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(my_deck.deal_card())
            if dealer_hand.get_value() > 21:
                outcome = "Dealer busts, you win. New deal?"
                score += 1
                in_play = False
                return score, outcome, in_play
            elif dealer_hand.get_value() >= player_hand.get_value():
                outcome = "Dealer wins. New deal?"
                score -= 1
                in_play = False
                return score, outcome, in_play
            else:
                outcome = "You win. New deal?"
                score += 1
                in_play = False
                return score, outcome, in_play
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    dealer_hand.draw(canvas, [0, 200])    
    player_hand.draw(canvas, [0, 400])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_SIZE)    
    canvas.draw_text(outcome,[50,75],20,"Black")
    canvas.draw_text("Score: "+str(score),[50,50],20,"Black")
    canvas.draw_text("BlackJack",[250,50],35,"Black")
    if outcome == "Dealer busts, you win. New deal?" or outcome == "You win. New deal?":
        canvas.draw_image(happy, (50, 50), (100,100), (50, 350), (100,100) )
        canvas.draw_image(bsad, (50, 50), (100,100), (50, 150), (100,100) )
    elif outcome=="Dealer wins. New deal?" or outcome == "You are busted. New Deal?":
        canvas.draw_image(sad, (50, 50), (100,100), (50, 350), (100,100) )
        canvas.draw_image(bhappy, (50, 50), (100,100), (50, 150), (100,100) )
    elif outcome = " ":
        canvas.draw_image(playing, (50, 50), (100,100), (50, 350), (100,100) )
        canvas.draw_image(bhappy, (50, 50), (100,100), (50, 150), (100,100) )
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
