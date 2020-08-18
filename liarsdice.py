'''
Liars' Dice
'''
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

class Game:

    def __init__(self):
    # Game Parameters
    # Sets the number of players and number of dice p. player
        self.numPlayers = 4 ; self.numDice = 5 ; self.dice = {}
        # Populates the dice for the round
        for num in range(self.numPlayers):
            self.dice[num] = []
            for dice in range(self.numDice):
                self.dice[num].append(np.random.randint(1,7))
        # Sets the rounds to zero
        self.rounds = 0
        self.bets = {}

    def makeMove(self, player):
        player.move(self)

class Player:

    def __init__(self, strat):
        self.strategy = strat

    def move(self, board):
        
