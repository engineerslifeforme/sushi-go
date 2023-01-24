""" Sushi go game"""

import math

from sushi_go.card import Deck, SCORING_TYPES, Pudding, Chopsticks
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
        players = [Player() for _ in range(self.player_quantity)]
        for index in range(3):
            print(f"Round {index+1}")
            self.play_round(players)
        self.score_pudding(players)
        self.choose_winner(players)

    @staticmethod
    def choose_winner(players: list):
        scores = [player.score for player in players]
        winning_score = max(scores)
        winning_score_quantity = scores.count(winning_score)
        if winning_score_quantity == 1:
            for index, player in enumerate(players):
                if player.score == winning_score:
                    winning_index = index
        else:
            winning_scorers = [player for player in players if player.score == winning_score]
            most_pudding_players = [index for index, player in enumerate(winning_scorers) if player.most_pudding]
            if len(most_pudding_players) == 1:
                winning_index = most_pudding_players[0]
            else:
                raise(ValueError("Tie!!!!"))
        print(f"Player #{winning_index} won!")
        return players[winning_index]
                        

    @staticmethod
    def score_pudding(players: list):
        pudding_quantities = [player.pudding_quantity for player in players]
        max_quantity = max(pudding_quantities)
        min_quantity = min(pudding_quantities)
        for index, player in enumerate(players):
            if player.pudding_quantity == max_quantity:
                pudding_score = math.floor(6 / pudding_quantities.count(max_quantity))
                player.score += pudding_score
                print(f"Player #{index} got {pudding_score} pudding points")
                player.most_pudding = True
            if player.pudding_quantity == min_quantity and len(players) > 2:
                pudding_score = math.floor(6 / pudding_quantities.count(min_quantity))
                player.score -= pudding_score
                print(f"Player #{index} lost {pudding_score} pudding points")
        return players

    def play_round(self, players: list):
        hands = self.deal()        
        for index, hand in enumerate(hands):
            players[index].hand = hand
        for turn in range(self.hand_size):
            print(f"Turn #{turn}")
            for index, player in enumerate(players):
                selected_cards = player.select_card()
                number_selected = len(selected_cards)
                assert(number_selected > 0), "At least one card must be selected!"
                player.keep += selected_cards
                if number_selected > 1:
                    # Will exception if no chopsticks
                    chopsticks = [card for card in player.keep if issubclass(type(card), Chopsticks)][0]
                    player.hand.append(chopsticks)
                    player.keep.remove(chopsticks)
                print(f"Player #{index} selected {selected_cards}")
            first_hand = players[0].hand
            for index, player in enumerate(players):
                if index == (len(players) - 1):
                    player.hand = first_hand
                else:
                    players[index].hand = players[index+1].hand
        self.score(players)

    @staticmethod
    def discard(players: list):
        for index, player in enumerate(players):
            player.pudding_quantity += len([card for card in player.keep if issubclass(type(card), Pudding)])
            player.keep = []
            print(f"Player #{index} has {player.pudding_quantity} pudding")
    
    @staticmethod
    def score(players: list):
        for index, player in enumerate(players):
            players_copy = players.copy()
            players_copy.remove(player)
            for CardType in SCORING_TYPES:
                player.score += CardType.score(player.keep, [other.keep for other in players_copy])
            print(f"Player #{index} score: {player.score}")

    def deal(self) -> list:
        hands = [[] for _ in range(self.player_quantity)]
        for _ in range(self.hand_size):
            for hand in hands:
                hand.append(self.deck.draw())
        return hands