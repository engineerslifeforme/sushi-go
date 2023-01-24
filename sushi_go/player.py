""" Sushi go player"""

class Player:

    def __init__(self):
        self.hand = []
        self.keep = []
        self.score = 0
        self.pudding_quantity = 0
        self.most_pudding = False

    def select_card(self) -> list:
        return [self.hand.pop()]