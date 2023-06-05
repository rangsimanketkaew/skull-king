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
        # card parameters
        self.num_players = players
        self.round = round
        self.values = []
        self.colors = []
        self.deck = []
        # player parameters
        self.players = { player+1 : [] for player in range(self.num_players)}
        self.players_scores = { player+1 : 0 for player in range(self.num_players)}

    @staticmethod
    def print_card(my_cards):
        print(my_cards)

    def start(self):
        self.form_deck()
        self.check_card()
        self.random_deck()
        # self.print_card(card.deck)
        self.distribute_card()

    def form_deck(self):
        # Normal cards
        self.values = [str(i + 1) for i in range(0, 13)]
        self.color = ["red", "yellow", "blue", "black"]

        # Special cards
        special_cards = [
            "white_flag",
            "white_flag",
            "white_flag",
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
        
        # Split the decks
        self.actual_deck = self.deck[:self.num_players*self.round]
        # Let's distribute card
        for i in range(self.num_players):
            self.players[i+1] = self.actual_deck[i::self.num_players]

    def scoring(self):
        return None

    def compare_card(self):
        return None
    
    def play(self):
        # loop over round
        for r in range(self.round):
            # loop over player
            for p in range(self.players):
                card = None
                while card is None:
                    try:
                        card = int(input("Which one? "))
                    except ValueError:
                        print("Try again!")
                        pass
                return None

round = 5
num_players = 5
card = Deck(players=num_players, round=round)
card.start()

print("Round: ", round)
print("Number of players: ", num_players)
pp.pprint(card.players)
print("")

card.play()
