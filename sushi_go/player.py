""" Sushi go player"""

class Player:

    def __init__(self, initial_hand: list):
        self.hand = initial_hand
        self.keep = []

    def select_card(self):
        selected_card = self.hand.pop()
        self.keep.append(selected_card)
        return selected_card