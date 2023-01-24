""" tests for game"""

from sushi_go.game import Game

class FakePlayer:

    def __init__(self, score: int = 0, most_pudding: bool = False, pudding: int = 0):
        self.score = score
        self.most_pudding = most_pudding
        self.pudding_quantity = pudding

def test_two_player_game():
    game = Game(2)
    game.play()

def test_three_player_game():
    game = Game(3)
    game.play()

def test_choose_winner():
    players = [FakePlayer(score=2), FakePlayer(score=3)]
    winner = Game.choose_winner(players)
    assert(winner.score == 3)
    winner = Game.choose_winner([
        FakePlayer(score=3, most_pudding=True),
        FakePlayer(score=3),
    ])
    assert(winner.most_pudding)

def test_score_pudding():
    players = Game.score_pudding([
        FakePlayer(pudding=1),
        FakePlayer(pudding=0),
    ])
    assert(players[0].score == 6)
    assert(players[1].score == 0)
    players = Game.score_pudding([
        FakePlayer(pudding=1),
        FakePlayer(pudding=1),
    ])
    assert(players[0].score == 3)
    assert(players[1].score == 3)
    players = Game.score_pudding([
        FakePlayer(pudding=1),
        FakePlayer(score=10, pudding=0),
        FakePlayer(pudding=2),
    ])
    assert(players[0].score == 0)
    assert(players[1].score == 4)
    assert(players[2].score == 6)
    players = Game.score_pudding([
        FakePlayer(score=8, pudding=0),
        FakePlayer(score=10, pudding=0),
        FakePlayer(pudding=2),
    ])
    assert(players[0].score == 5)
    assert(players[1].score == 7)
    assert(players[2].score == 6)