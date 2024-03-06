from collections import Counter

def accolade(play: str) -> int:
    if play.count("J") == 5:
        return 5
    
    counter = Counter(play)
    most_common_list = counter.most_common(2)
    most_common = most_common_list[0][0] if most_common_list[0][0] != "J" else most_common_list[1][0]
    play = play.replace("J", most_common)
    
    counts = [play.count(char) for char in play]
    max_counts = max(counts)
    match max_counts:
        case 5: # 5 of a kind
            return 5
        case 4: # 4 of a kind
            return 4
        case 3: # Full house, or 3 of a kind
            if 2 in counts:
                return 3.5
            else:
                return 3
        case 2: # Two pairs, or One pair
            if counts.count(2) == 4:
                return 2.5
            else:
                return 2
        case 1: # High card
            return 1
        

def mapped(play: str) -> str:
    face_card_map = {
        "T": "A",
        "J": "1",
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