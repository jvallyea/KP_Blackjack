from matplotlib import pyplot
import math
from random import shuffle

# Class for a card in a deck
# A card has 2 fields: a value, and a suit (both as strings)
class Card():
    # Initializes the class
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

# Class for a deck
# The primary field for a deck is .cards, which contains a list of
# cards found in the deck
class Deck():
    # Initializes the class
    def __init__(self):
        # Parameters for housekeeping
        self.royals = ['K','Q','J']
        self.suits = ['C','D','H','S']
        self.vals = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        cards = []
        self.cards = cards
        # This pulls the top card out of the deck
        def next_card(self):
            return self.cards.pop(0)
        # Restores the deck
        def fill(self):
            self.cards = []
            for val in vals:
                for suit in suits:
                    self.cards.append(Card(val,suit))
                    self.cards.append(Card(val,suit))
                    self.cards.append(Card(val,suit))

# Class for the blackjack Table
class Table(deck,player_list):
    # Initializes the Table
    def __init__(self):
        # The table holds the players on the table, the deck, and the pot size
        self.players = player_list
        self.stack = deck
        self.pot = 0

    # Deals to all players
    def deal(self):
        for player in self.players:
            card1 = self_stack.next_card()
            card2 = self_stack.next_card()
            player.hand = [card1, card2]
            player.cash -= 10
            self.pot += 10



class AI():
    # Initializes the AI class
    def __init__(self):
        self.history = []
        self.cash = 1000
        self.hand = []
        # Player status
        # 0; idle
        # 1: active, betting
        # 2: fold
        # 3: bust
        self.status = 0
    # Wipes all knowledge of cards played
    def flush_history(self):
        self.history = []
    # Method to store open cards in history
    def store_data(self, cards_played):
        for card in cards_played:
            self.history.append(card)
    # Method to calculate the value of a hand
    def hand_value(self, hand, deck):
        hand_value = 0
        if 'A' in hand:

        else:
            for card in hand:
                if card in deck.royals:
                    hand_value += 10
                else:
                    hand_value += int(card)
            return [hand_value]
