scratchcards = open(0).read().strip().splitlines()

def calculate_points(n):
    if n == 0:
        return 0
    total = 1
    n -= 1
    while (n > 0):
        total *= 2
        n -=1
    return total

total_points = 0
for card in scratchcards:
    halves = card.split("|")
    winning_numbers = set(halves[0].split(":")[1].strip().split())
    personal_numbers = halves[1].strip().split()

    num_matches = 0
    for num in personal_numbers:
        if num in winning_numbers:
            num_matches += 1
    
    total_points += calculate_points(num_matches)

print(total_points)


"""
alt solution
total = 0

for hands in open(0):
    hands = hands.split(":")[1].strip()
    winning_numbers, my_hand = [list(map(int, h.split())) for h in hands.split("|")]
    j = sum(q in winning_numbers for q in my_hand)
    if j > 0:
        total += 2 ** (j - 1)

print(total)
"""
