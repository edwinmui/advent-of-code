seeds, *blocks = open(0).read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    next_stage = []
    for ss, se in seed_ranges:
        for a, b, c in ranges:
            # find intersection
            rs, re = b, b + c
            os = max(ss, rs)
            oe = min(se, re)
            if os < oe:
                next_stage.append((os - b + a, oe - b + a))
                # check if exists non-intersected seed ranges
                if se > oe:
                    seed_ranges.append((oe, se))
                if ss < os:
                    seed_ranges.append((ss, os))
                break
        else:
            next_stage.append((ss, se))
    seed_ranges = next_stage

print(min(seed_ranges)[0])



"""
for each block, for each line, there are two options for a given seed_range:
1. the seed_range matches an interval, gets mapped and moved onto next stage
2. the seed_range doesn't match any interval, needs to be test on another line

seeds:
45 - 55
50 - 55 maps, put those through to next block/stage
45 - 50 doesn't map, need to test with remaining blocks/stages

maps:
50 - 98
98 - 100
"""