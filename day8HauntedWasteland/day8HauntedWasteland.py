rl_algo, network = open(0).read().split("\n\n")

grid = {}
for line in network.splitlines():
    key, val = line.split(" = ")
    grid[key] = val[1:-1].split(", ")

curr_key = "AAA"
total = 0
index = 0
while curr_key != "ZZZ":
    if index == len(rl_algo):
        index = 0
    l_or_r = 0 if rl_algo[index] == "L" else 1
    curr_key = grid[curr_key][l_or_r]
    index += 1
    total += 1

print(total)

"""
len = 2
curr_key = "GGG"
index = 0
next_key = "GGG"

Test
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)

"""