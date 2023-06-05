# 2023.06.05
# Rangsiman Ketkaew

import itertools
import random

class Deck:
    """ Skull king's card decks contain normal cards of 4 differet colors: 
        red, yellow, blue, and black, each with value ranging from 1 to 13.
        The rest are special cards whose number of each card is as follows:

        white_flags = 3
        mermaid = 2
        king = 4
        king_flag = 2
        skull_king = 1

        In total we have 64 cards
    """
    def __init__(self, players: int, round: int) -> None:
        self.values = []
        self.colors = []
        self.deck = []
    
    # @staticmethod
    def check_card(self):
        assert len(self.deck) == 64

    def form_deck(self):
        # Normal cards
        self.values = [str(i+1) for i in range(0,13)]
        self.color = ['red', 'yellow', 'blue', 'black']
        
        # Special cards
        special_cards = [
            'white_flags', 'white_flags', 'white_flags',
            'mermaid', 'mermaid',
            'king', 'king', 'king', 'king', 
            'king_flag', 'king_flag',
            'skull_king'
        ]

        # Combine all cards
        # self.deck = [[v + ' of ' + c,v] for c in self.colors for v in self.values]
        self.deck = list(itertools.product(self.color, self.values))
        print(self.deck)
        self.deck = self.deck + special_cards

    def random_deck(self):
        self.deck = random.shuffle(self.deck)

    def print_card(self):
        print(self.deck)

num_of_players = 4
num_round = 1
card = Deck(players=num_of_players, round=num_round)
card.form_deck()
card.random_deck()
card.print_card()
