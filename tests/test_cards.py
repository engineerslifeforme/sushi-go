from sushi_go.card import (
    Deck,
    Tempura,
    Sashimi,
    Dumpling,
    MakiRolls,
    SalmonNigiri,
    EggNigiri,
    SquidNigiri,
    Wasabi,
    Nigiri,
)

def test_deck():
    a_deck = Deck()
    assert(len(a_deck.cards) == 108)

def test_filter_type():
    cards = [Tempura(), Sashimi()]
    others = [[Tempura(), Sashimi()]]
    filtered_cards, filtered_others = Tempura.filter_type(cards, others)
    assert(len(filtered_cards) == 1)
    assert(issubclass(type(filtered_cards[0]), Tempura))
    assert(not issubclass(type(filtered_cards[0]), Sashimi))
    assert(len(filtered_others) == 1)
    assert(len(filtered_others[0]) == 1)

def test_tempura():
    assert(Tempura.score([], [[]]) == 0)
    assert(Tempura.score(2 * [Tempura()], []) == 5)
    assert(Tempura.score(3 * [Tempura()], []) == 5)
    assert(Tempura.score(4 * [Tempura()], []) == 10)

def test_sashimi():
    assert(Sashimi.score([], [[]]) == 0)
    assert(Sashimi.score(3 * [Sashimi()], []) == 10)
    assert(Sashimi.score(4 * [Sashimi()], []) == 10)
    assert(Sashimi.score(6 * [Sashimi()], []) == 20)

def test_dumpling():
    CardType = Dumpling
    assert(CardType.score([], [[]]) == 0)
    assert(CardType.score(1 * [CardType()], []) == 1)
    assert(CardType.score(2 * [CardType()], []) == 3)
    assert(CardType.score(3 * [CardType()], []) == 6)
    assert(CardType.score(4 * [CardType()], []) == 10)
    assert(CardType.score(5 * [CardType()], []) == 15)
    assert(CardType.score(6 * [CardType()], []) == 15)

def test_maki():
    assert(MakiRolls.score([], [[]]) == 0)
    assert(MakiRolls.score([MakiRolls(2)], [[]]) == 6)
    assert(MakiRolls.score([MakiRolls(2)], [[MakiRolls(2)]]) == 3)
    assert(MakiRolls.score([MakiRolls(2)], [[MakiRolls(3)], [MakiRolls(3)]]) == 0)
    assert(MakiRolls.score([MakiRolls(1)], [[MakiRolls(2)]]) == 3)
    assert(MakiRolls.score([MakiRolls(1)], [[MakiRolls(3)], [MakiRolls(2)]]) == 0)

def test_nigiri():
    assert(Nigiri.score([], [[]]) == 0)
    assert(Nigiri.score([EggNigiri()], [[]]) == 1)
    assert(Nigiri.score([SalmonNigiri()], [[]]) == 2)
    assert(Nigiri.score([SquidNigiri()], [[]]) == 3)
    assert(Nigiri.score([SalmonNigiri(), Wasabi()], [[]]) == 6)
    assert(Nigiri.score([SalmonNigiri(), Wasabi(), EggNigiri()], [[]]) == 7)
    assert(Nigiri.score([SalmonNigiri(), Wasabi(), Wasabi()], [[]]) == 6)