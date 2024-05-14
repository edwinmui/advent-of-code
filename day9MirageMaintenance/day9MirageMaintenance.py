report = open(0).read().splitlines()


# Returns extrapolated value of a given list
def extrapolate(values: list[int]) -> int:
    # Base case
    if all(n == 0 for n in values):
        return 0

    diffs = [y - x for x, y in zip(values, values[1:])]

    return values[-1] + extrapolate(diffs)


total_sum = 0
for line in report:
    line = list(map(int, line.split()))
    total_sum += extrapolate(line)

print(total_sum)

"""
0 3 6 9 12 15 -> 18
3 3 3 3 3 -> 3
0 0 0 0
"""


"""
Time: O(n^2)

Solution:
1. Calculate differences array
2. Recursively grab the extrapolated value of the differences array
3. Add the extrapolated value of differences array to curr_arr[-1]. Return that value
"""
