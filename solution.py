card_dict = {}

for i, hands in enumerate(open(0)):
    # have at least 1 original card
    if i not in card_dict:
        card_dict[i] = 1
    
    hands = hands.split(":")[1].strip()
    winning_numbers, my_hand = [list(map(int, h.split())) for h in hands.split("|")]
    j = sum(q in winning_numbers for q in my_hand)
    
    for n in range(i + 1, i + j + 1):
        card_dict[n] = card_dict.get(n, 1) + card_dict[i]

print(sum(card_dict.values()))