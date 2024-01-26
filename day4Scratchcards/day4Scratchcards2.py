from collections import deque

scratchcards = open(0).read().strip().splitlines()
N = len(scratchcards)

grid = []

for i in range(N):
    winning_numbers_and_personal_numbers = scratchcards[i].split(":")[1]
    winning_numbers = set(winning_numbers_and_personal_numbers.split("|")[0].strip().split())
    personal_numbers = winning_numbers_and_personal_numbers.split("|")[1].strip().split()
    grid.append([winning_numbers, personal_numbers])

total_cards = 0
memo = {}
q = deque()

def count_wins(card_number):
    if card_number in memo:
        return memo[card_number]
    wins = 0
    winning_cards = grid[card_number][0]
    my_cards = grid[card_number][1]
    for card in my_cards:
        if card in winning_cards:
            wins += 1
    memo[card_number] = wins
    return memo[card_number]

for i in range(N):
    q.append(i)
    while(q):
        next_card = q.popleft()
        total_cards += 1
        num_cards_won = count_wins(next_card)
        for j in range(num_cards_won):
            q.append(next_card + j + 1)

print(total_cards)


"""
Sexy way

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
"""