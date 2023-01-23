""" Sushi go cards"""

import math

from random import shuffle

class Card:
    
    def __repr__(self) -> str:
        return self.__class__.__name__

    @classmethod
    def score(cls, cards: list, other_keeps: list) -> int:
        raise NotImplementedError()

    @classmethod
    def filter_type(cls, cards: list, other_keeps: list) -> tuple:
        filtered_cards = [card for card in cards if issubclass(type(card), cls)]
        filtered_keeps = []
        for keep_set in other_keeps:
            filtered_keeps.append([card for card in keep_set if issubclass(type(card), cls)])
        return filtered_cards, filtered_keeps

class Tempura(Card):
    
    @classmethod
    def score(cls, cards: list, other_keeps: list) -> int:
        filtered_cards, _ = cls.filter_type(cards, other_keeps)
        return math.floor(len(filtered_cards) / 2) * 5

class Sashimi(Card):
    
    @classmethod
    def score(cls, cards: list, other_keeps: list) -> int:
        filtered_cards, _ = cls.filter_type(cards, other_keeps)
        return math.floor(len(filtered_cards) / 3) * 10

class Dumpling(Card):
    
    @classmethod
    def score(cls, cards: list, other_keeps: list) -> int:
        filtered_cards, _ = cls.filter_type(cards, other_keeps)
        score_map = {
            0: 0,
            1: 1,
            2: 3,
            3: 6,
            4: 10,
        }
        try:
            score = score_map[len(filtered_cards)]
        except KeyError:
            score = 15
        return score

class MakiRolls(Card):

    def __init__(self, quantity: int):
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"{super().__repr__()}({self.quantity})"

    @classmethod
    def score(cls, cards: list, other_keeps: list) -> int:
        filtered_cards, filtered_keeps = cls.filter_type(cards, other_keeps)
        try:
            quantity = sum([card.quantity for card in filtered_cards])
        except:
            quantity = 0
        if quantity == 0:
            return 0
        
        quantities = [sum([card.quantity for card in other_cards]) for other_cards in filtered_keeps] + [quantity]
        max_quantity = max(quantities)
        number_of_max = quantities.count(max_quantity)

        if number_of_max > 1:
            if quantity == max_quantity:
                return math.floor(6 / number_of_max)
            else:
                return 0
        else:
            if quantity == max_quantity:
                return 6
            else:
                quantities.remove(max_quantity)
                second_max = max(quantities)            
                if quantity == second_max:
                    return math.floor(3 / (quantities.count(second_max)))
                else:
                    return 0


class Nigiri(Card):
    value = 0

    @classmethod
    def score(cls, cards: list, other_keeps: list) -> int:
        nigiri_cards, _ = Nigiri.filter_type(cards, other_keeps)
        wasabi_cards, _ = Wasabi.filter_type(cards, other_keeps)
        nigiri_values = [card.value for card in nigiri_cards]
        nigiri_values.sort(reverse=True)
        for index, _ in enumerate(wasabi_cards):
            try:
                nigiri_values[index] = nigiri_values[index] * 3
            # Extra wasabi do nothing
            except IndexError:
                break
        return sum(nigiri_values)

class SalmonNigiri(Nigiri):
    value = 2

class SquidNigiri(Nigiri):
    value = 3

class EggNigiri(Nigiri):
    value = 1

class Pudding(Card):
    pass

class Chopsticks(Card):
    pass

class Wasabi(Card):
    pass

CARD_TYPES = [
    Tempura,
    Sashimi,
    Dumpling,
    MakiRolls,
    Nigiri,
    Pudding,
    Wasabi,
    Chopsticks,
]

class Deck:

    def __init__(self):
        self.cards = 14 * [Tempura()] +\
            14 * [Sashimi()] +\
            14 * [Dumpling()] +\
            12 * [MakiRolls(2)] +\
            8 * [MakiRolls(3)] +\
            6 * [MakiRolls(1)] +\
            10 * [SalmonNigiri()] +\
            5 * [SquidNigiri()] +\
            5 * [EggNigiri()] +\
            10 * [Pudding()] +\
            6 * [Wasabi()] +\
            4 * [Chopsticks()]
        shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()

