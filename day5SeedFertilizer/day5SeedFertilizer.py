seeds, *blocks = open(0).read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

for block in blocks:   # block = ["3 2 1"] ["3 2 1"]
    ranges = []
    for line in block.splitlines()[1:]: # line = ["3 2 1"]
        ranges.append(list(map(int, line.split()))) # range = [3, 2, 1]
    curr_stage = []
    for seed in seeds:
        for a, b, c in ranges:
            if seed >= b and seed < b + c:
                curr_stage.append(a + (seed - b))
                break
        else:
            curr_stage.append(seed)
    seeds = curr_stage

print(min(seeds))


# old code
# # assigns seeds to the first line of seeds, and then unpacks the rest of split("\n\n") and assigns the
# # list of stages to "blocks"
# seeds, *blocks = open(0).read().split("\n\n")

# location_list = []

# mappings_grid = []
# for block in blocks:
#     mappings_grid.append(block.split(":")[1].strip().split("\n"))

# seeds = seeds.split(":")[1].strip().split()
# for seed in seeds:
#     prev_num = int(seed)
#     for mapping_stage in mappings_grid:
#         for mapping in mapping_stage:
#             mapping = mapping.strip().split()
#             if prev_num > int(mapping[1]) and prev_num < int(mapping[1]) + int(mapping[2]):
#                 prev_num = int(mapping[0]) + (prev_num - int(mapping[1]))
#                 break
#     location_list.append(prev_num)

# print(min(location_list))
