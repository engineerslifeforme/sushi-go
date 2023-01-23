""" tests for game"""

from sushi_go.game import Game

def test_game():
    game = Game(2)
    game.play()