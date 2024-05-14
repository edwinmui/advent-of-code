report = open(0).read().splitlines()


# Returns extrapolated value of a given list
def extrapolate(values: list[int], temp: int = 0, extrap_sum: int = 0) -> int:
    # Base case
    if all(n == 0 for n in values):
        return 0

    diffs = [y - x for x, y in zip(values, values[1:])]
    extrap_sum += values[0] - extrapolate(diffs, extrap_sum)

    return extrap_sum


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
Solution:
Same as previous Part, but just subract instead of add the last digit
"""
