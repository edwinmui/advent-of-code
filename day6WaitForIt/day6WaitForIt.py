races = open(0).read()

times, distances = [list(map(int, line.split(":")[1].split())) for line in races.splitlines()]

winning_total = 1
for time, distance in zip(times, distances):
    curr_combos = 0
    for i in range(0, time-1):
        curr_distance = (time - i) * i
        if curr_distance > distance:
            curr_combos += 1
    winning_total *= curr_combos

print(winning_total)