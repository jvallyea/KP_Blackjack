# Console-Run Blackjack

# Import Statements
from random import randint

# Instantiates a new deck composed of 4 standard 52 card decks together
def new_deck():
    standard_deck = []
    standard_suit = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    for i in range(4):
        for card in standard_suit:
            standard_deck.append(card)
    deck = []
    for i in range(4):
        for card in standard_deck:
            deck.append(card)
    return deck

# Deals cards to the dealer and to the player.
def deal(deck):
    your_hand = []
    dealer_hand = []
    for i in range(2):
        j = randint(0,len(deck)-1)
        your_hand.append(deck[j])
        deck.pop(j)
    for i in range(2):
        j = randint(0,len(deck)-1)
        dealer_hand.append(deck[j])
        deck.pop(j)
    return your_hand, dealer_hand, deck

# Checks the sum of the hand (assuming ace = 1)
def check_hand(hand):
    royals = ['J','Q','K']
    sum = 0
    for card in hand:
        if card in royals:
            card = 10
        if card == 'A':
            card = 1
        sum += int(card)
    return sum

# Checks if a given hand has an ace in it
def has_ace(hand):
    has_ace = False
    for card in hand:
        if card == 'A':
            has_ace = True
    return has_ace

# Checks the sum of the hand (assuming ace = 11)
def check_hand_ace(hand):
    royals = ['J','Q','K']
    sum = 0
    for card in hand:
        if card in royals:
            card = 10
        if card == 'A':
            card = 11
        sum += int(card)
    return sum

# Replaces the value of the ace in a hand with 11
def replace_ace(hand):
    new_hand = []
    for card in hand:
        if card == 'A':
            new_hand.append(11)
        else:
            new_hand.append(card)
    return new_hand

# Hits a hand with a card
def hit(deck, hand):
    i = randint(0,len(deck)-1)
    hand.append(deck[i])
    deck.pop(i)
    return deck, hand

# Updates print statements for your hand and dealers hand
def pre_update(your_hand, dealer_hand):
    hand1 = "Your Hand: "
    hand2 = "Dealers Hand: "
    for card in your_hand:
        hand1 += str(card)
        hand1 += " "
    hand2 += str(dealer_hand[0])
    hand2 += " []"
    print hand1 + hand2

# Updates print statments for your hand and dealers hand
def post_update(your_hand, dealer_hand):
    hand1 = "Your Hand: "
    hand2 = "Dealers Hand: "
    for card in your_hand:
        hand1 += str(card)
        hand1 += " "
    for card in dealer_hand:
        hand2 += str(card)
        hand2 += " "
    print hand1 + hand2

# Calculates how the dealer should play their hand
def dealer_math(your_hand, dealer_hand):
    while True:
        if check_hand(dealer_hand) > check_hand(your_hand):
            post_update(your_hand, dealer_hand)
            break
        else:
            hit(deck, dealer_hand)

# Runs the final calculations and print statments to see who won the hand
def calculate(your_hand, dealer_hand):
    if has_ace(your_hand) == True and check_hand_ace(your_hand) <= 21:
        your_hand = replace_ace(your_hand)
    if has_ace(dealer_hand) == True and check_hand_ace(dealer_hand) <= 21:
        dealer_hand = replace_ace(dealer_hand)
    if check_hand(dealer_hand) > 21:
        print "Dealer busted. You win! "
        return -1
    elif check_hand(dealer_hand) > check_hand(your_hand):
        print "Dealer wins. "
        return 1
    elif check_hand(your_hand) > check_hand(dealer_hand):
        print "You win!"
        return -1
    elif check_hand(your_hand) == check_hand(your_hand):
        print "It's a tie."
        return 0
    else:
        print "Error: Returning to deal screen. "

# Code to execute the game on a while True loop. To exit, type exit.
while True:
    print "Welcome to the new game of blackjack!"
    deck = new_deck()
    count = 0
    dealer = 0
    while count < 10:
        text = raw_input("Please type 'deal' to play, 'exit' to quit:  ")
        if text == 'deal':
            your_hand, dealer_hand, deck = deal(deck)
            while check_hand(your_hand) <= 21:
                pre_update(your_hand, dealer_hand)
                text = raw_input("Please type 'hit' or 'stay'.  ")
                if text == 'hit':
                    deck, your_hand = hit(deck, your_hand)
                    if check_hand(your_hand) > 21:
                        pre_update(your_hand, dealer_hand)
                        print "I'm sorry. You busted.  "
                        count += 1
                        dealer += 1
                        break
                if text == 'stay':
                    dealer_math(your_hand, dealer_hand)
                    dealer += calculate(your_hand, dealer_hand)
                    count += 1
                    break
        elif text == 'exit':
            exit()
        else:
            print "I'm sorry, I didn't get that."
    if dealer > 0:
        print "I'm sorry. The dealer won this game. Play again?"
    if dealer == 0:
        print "This game was a tie. Play again?"
    if dealer < 0:
        print "Congratulations! You won this game. Play again?"
