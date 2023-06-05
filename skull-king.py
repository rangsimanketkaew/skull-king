# 2023.06.05
# Rangsiman Ketkaew

import itertools
import random
import pprint as pp


class Deck:
    """Skull king's card decks contain normal cards of 4 differet colors:
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
        self.num_players = players
        self.round = round
        self.values = []
        self.colors = []
        self.deck = []

    @staticmethod
    def print_card(my_cards):
        print(my_cards)

    def form_deck(self):
        # Normal cards
        self.values = [str(i + 1) for i in range(0, 13)]
        self.color = ["red", "yellow", "blue", "black"]

        # Special cards
        special_cards = [
            "white_flags",
            "white_flags",
            "white_flags",
            "mermaid",
            "mermaid",
            "king",
            "king",
            "king",
            "king",
            "king_flag",
            "king_flag",
            "skull_king",
        ]

        # Combine all cards
        # self.deck = [[v + ' of ' + c,v] for c in self.colors for v in self.values]
        self.deck = list(itertools.product(self.color, self.values))
        self.deck = self.deck + special_cards

    def check_card(self):
        assert len(self.deck) == 64

    def random_deck(self):
        random.shuffle(self.deck)

    def distribute_card(self):
        self.players = { player+1 : [] for player in range(self.num_players)}
        # Split the decks
        self.actual_deck = self.deck[:self.num_players*self.round]
        # Let's distribute card
        for i in range(self.num_players):
            self.players[i+1] = self.actual_deck[i::self.num_players]

round = 5
num_players = 5
card = Deck(players=num_players, round=round)
card.form_deck()
card.check_card()
card.random_deck()
# card.print_card(card.deck)
card.distribute_card()

print("Round: ", round)
print("Number of players: ", num_players)
pp.pprint(card.players)
