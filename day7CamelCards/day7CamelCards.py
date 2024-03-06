def accolade(play: str) -> int:
    counts = [play.count(char) for char in play]
    max_counts = max(counts)
    match max_counts:
        case 5: # 5 of a kind
            return 7
        case 4: # 4 of a kind
            return 6
        case 3: # Full house, or 3 of a kind
            if 2 in counts:
                return 5
            else:
                return 4
        case 2: # Two pairs, or One pair
            if counts.count(2) == 4:
                return 3
            else:
                return 2
        case 1: # High card
            return 1
        

def mapped(play: str) -> str:
    face_card_map = {
        "T": "A",
        "J": "B",
        "Q": "C",
        "K": "D",
        "A": "E"
    }
    mapped_hand = "".join(face_card_map.get(char, char) for char in play)

    return mapped_hand


def strength(play: str) -> tuple:

    return (accolade(play), mapped(play))


inp = open(0).read().splitlines()
plays = []
for line in inp:
    hand_and_bid = line.split()
    plays.append((hand_and_bid[0], int(hand_and_bid[1])))
plays.sort(key = lambda play: strength(play[0]))
total = sum(rank * play[1] for rank, play in enumerate(plays, 1))

print(total)

"""
Formula:
sum(bid * rank)

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""