from itertools import permutations


card_types = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]
jind = card_types.index("J")


def get_type(cards):
    jcount = 0
    if cards.count(jind) != 0:
        jcount = cards.count(jind)
    counts = {}
    for card in cards:
        counts[card] = counts.get(card, 0) + 1

    counts[jind] = 0

    c = sorted(counts.values(), reverse=True)

    c[0] += jcount

    if c[0] == 5:
        return 7
    elif c[0] == 4:
        return 6
    elif c[0] == 3 and c[1] == 2:
        return 5
    elif c[0] == 3:
        return 4
    elif c[0] == 2 and c[1] == 2:
        return 3
    elif c[0] == 2:
        return 2
    else:
        return 1

class Hand:
    def __init__(self, cards, bid):
        self.cards = [card_types.index(card) for card in cards]
        self.bid = int(bid)
        self.type = 1
        self.type = get_type(self.cards)




hands = []
with open("7.txt", "r") as f:
    for line in f:
        h, bid = line.strip().split()
        hands.append(Hand(h, bid))

tuples = sorted([(hand.type, hand.cards, hand.bid) for hand in hands])

total = 0
for rank, t in enumerate(tuples, 1):
    total += rank * t[2]
print(total)
