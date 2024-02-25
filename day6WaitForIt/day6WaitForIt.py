races = open(0).read()

times, distances = [list(map(int, line.split(":")[1].split())) for line in races.splitlines()]
t_d_pairs = []
for i in range(len(times)):
    t_d_pairs.append((times[i], distances[i]))

winning_total = None
for time, distance in t_d_pairs:
    curr_combos = 0
    for i in range(0, time-1):
        curr_distance = (time - i) * i
        if curr_distance > distance:
            curr_combos += 1
    winning_total = curr_combos if not winning_total else winning_total * curr_combos

print(winning_total)