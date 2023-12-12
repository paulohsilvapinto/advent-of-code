from collections import defaultdict
from collections import namedtuple

from commons.utils import read_input

Game = namedtuple("Game", ["hand", "bid", "hand_strength"])
CARD_STRENGTH = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "T": "D",
    "9": "E",
    "8": "F",
    "7": "G",
    "6": "H",
    "5": "I",
    "4": "J",
    "3": "K",
    "2": "L",
    "J": "M",
}


def classify_hand_strength(cards):
    counter = defaultdict(int)
    for card in cards:
        counter[card] += 1

    # Reassign joker
    j_count = counter.get("J", None)
    if j_count and j_count != 5:
        del counter["J"]
        best_card = max(counter, key=counter.get)
        counter[best_card] += j_count

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
    elif distribution == [1, 1, 1, 1, 1]:
        return "G"  # "high_card"
    else:
        raise Exception(f"Distribution scenario not found for hand {cards} and counter {counter}")


def classify_cards_strength(cards):
    strength = ""
    for card in cards:
        strength += CARD_STRENGTH[card]
    return strength


games = read_input(day_number=7)
games_list = []
for game in games:
    hand, bid = game.split()
    hand = hand.upper()
    hand_strength = classify_hand_strength(hand) + classify_cards_strength(hand)
    games_list.append(Game(hand, int(bid), hand_strength))

ranked_games = sorted(games_list, key=lambda game: game.hand_strength, reverse=True)
# print(ranked_games)

total_winnings = sum([(rank + 1) * game.bid for rank, game in enumerate(ranked_games)])
print(total_winnings)
