races = open(0).read()

times, distances = [list(map(int, line.split(":")[1].split())) for line in races.splitlines()]
time = int("".join(map(str, times)))
distance = int("".join(map(str, distances)))

num_combos = None
for i in range(time):
    curr_distance = (time - i) * i
    if curr_distance > distance:
        num_combos = (time + 1) - (i * 2)
        break

print(num_combos)