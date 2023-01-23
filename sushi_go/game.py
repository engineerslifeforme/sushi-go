""" Sushi go game"""

from sushi_go.card import Deck
from sushi_go.player import Player

class Game:

    def __init__(self, players: int):
        self.deck = Deck()
        self.player_quantity = players
        # player quantity: initial hand size
        hand_sizes = {
            2: 10,
            3: 9,
            4: 8,
            5: 7,
        }
        try:
            self.hand_size = hand_sizes[self.player_quantity]
        except KeyError:
            print(f"Invalid player quantity: {self.player_quantity}")
            raise

    def play(self):
        hands = self.deal()
        players = [Player(hand) for hand in hands]
        for turn in range(self.hand_size):
            print(f"Turn #{turn}")
            for index, player in enumerate(players):
                print(f"Player #{index} selected {player.select_card()}")
        self.score(players)

    def score(cards: list):
        pass            

    def deal(self) -> list:
        hands = [[] for _ in range(self.player_quantity)]
        for _ in range(self.hand_size):
            for hand in hands:
                hand.append(self.deck.draw())
        return hands