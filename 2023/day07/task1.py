from collections import defaultdict
from collections import namedtuple

from commons.utils import read_input

Game = namedtuple("Game", ["hand", "bid", "hand_strength"])
CARD_STRENGTH = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
}


def classify_hand_strength(cards):
    counter = defaultdict(int)
    for card in cards:
        counter[card] += 1

    distribution = sorted(counter.values())

    if distribution == [5]:
        return "A"  # "five_of_a_kind"
    elif distribution == [1, 4]:
        return "B"  # "four_of_a_kind"
    elif distribution == [2, 3]:
        return "C"  # "full_house"
    elif distribution == [1, 1, 3]:
        return "D"  # "three_of_a_kind"
    elif distribution == [1, 2, 2]:
        return "E"  # "two_pairs"
    elif distribution == [1, 1, 1, 2]:
        return "F"  # "one_pair"
    else:
        return "G"  # "high_card"


def classify_cards_strength(cards):
    strength = ""
    for card in cards:
        strength += CARD_STRENGTH[card]
    return strength


games = read_input(year=2023, day_number=7)
games_list = []
for game in games:
    hand, bid = game.split()
    hand = hand.upper()
    hand_strength = classify_hand_strength(hand) + classify_cards_strength(hand)
    games_list.append(Game(hand, int(bid), hand_strength))

ranked_games = sorted(games_list, key=lambda game: game.hand_strength, reverse=True)

total_winnings = sum([(rank + 1) * game.bid for rank, game in enumerate(ranked_games)])
print(total_winnings)
