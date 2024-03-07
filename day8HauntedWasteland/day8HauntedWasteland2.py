from collections import Counter

rl_algo, network = open(0).read().split("\n\n")

grid = {}
for line in network.splitlines():
    key, val = line.split(" = ")
    grid[key] = val[1:-1].split(", ")

num_steps_list = []

def calc_num_steps(rl_algo: str, curr_key: str):
    total = 0
    index = 0
    while curr_key[-1] != "Z":
        if index == len(rl_algo):
            index = 0
        l_or_r = 0 if rl_algo[index] == "L" else 1
        curr_key = grid[curr_key][l_or_r]
        index += 1
        total += 1

    return total

for key in grid:
    if key[-1] == "A":
        num_steps_list.append(calc_num_steps(rl_algo, key))


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    return factors

def lcm(numbers):
    factors_count = Counter()
    for num in numbers:
        factors = Counter(prime_factors(num))
        factors_count |= factors    # gets the intersection

    lcm = 1
    for factor, count in factors_count.items():
        lcm *= factor ** count
    return lcm

print(lcm(num_steps_list))

"""
in python 3.9, could also import lcm() function from the math library (built-in to python)

"""