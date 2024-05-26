from collections import deque

# grid = open("test.txt", "r").read().strip().splitlines()

grid = open(0).read().strip().splitlines()


def find_S(grid: list[str]) -> tuple[int, int]:
    N = len(grid)
    M = len(grid[0])
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "S":
                return i, j

    return None


def is_allowed(r, c) -> bool:
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False

    return True


sr, sc = find_S(grid)
q = deque()
loop = set()
loop.add((sr, sc))
q.append((sr, sc))
potential_S = {"|", "-", "L", "J", "7", "F"}

while q:
    cr, cc = q.popleft()
    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)

    # Up
    ur, uc = cr + up[0], cc + up[1]
    if (
        (ur, uc) not in loop
        and is_allowed(ur, uc)
        and grid[cr][cc] in "S|LJ"
        and grid[ur][uc] in "|7F"
    ):
        loop.add((ur, uc))
        q.append((ur, uc))
        if grid[cr][cc] == "S":
            potential_S &= {"|", "L", "J"}

    # Right
    rr, rc = cr + right[0], cc + right[1]
    if (
        (rr, rc) not in loop
        and is_allowed(rr, rc)
        and grid[cr][cc] in "S-LF"
        and grid[rr][rc] in "-J7"
    ):
        loop.add((rr, rc))
        q.append((rr, rc))
        if grid[cr][cc] == "S":
            potential_S &= {"-", "L", "F"}

    # Down
    dr, dc = cr + down[0], cc + down[1]
    if (
        (dr, dc) not in loop
        and is_allowed(dr, dc)
        and grid[cr][cc] in "S|7F"
        and grid[dr][dc] in "|LJ"
    ):
        loop.add((dr, dc))
        q.append((dr, dc))
        if grid[cr][cc] == "S":
            potential_S &= {"|", "7", "F"}

    # Left
    lr, lc = cr + left[0], cc + left[1]
    if (
        (lr, lc) not in loop
        and is_allowed(lr, lc)
        and grid[cr][cc] in "S-J7"
        and grid[lr][lc] in "-LF"
    ):
        loop.add((lr, lc))
        q.append((lr, lc))
        if grid[cr][cc] == "S":
            potential_S &= {"-", "J", "7"}

assert len(potential_S) == 1
(S,) = potential_S

# Replaces S with the correct, unhidden pipe
grid[sr] = grid[sr].replace("S", S)

# Replace non loop chars with period
grid = [
    "".join([ch if (r, c) in loop else "." for c, ch in enumerate(row)])
    for r, row in enumerate(grid)
]

outside = set()
for r, row in enumerate(grid):
    within = False
    up = None
    for c, ch in enumerate(row):
        if ch == "|":
            assert up is None
            within = not within
        elif ch == "-":
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass
        else:
            raise RuntimeError(f"unexpected character (horizontal): {ch}")

        if not within:
            outside.add((r, c))

total = len(grid) * len(grid[0])
solution = total - len(loop | outside)
print("\n".join(grid))
print(solution)

"""
|-LJ7F
For each direction (e.g. up), check:
0. If coordinate above is not in seen
1. If allowed to move in that direction
2. If current piece allows to go in that direction
3. If piece above allows to go in that direction

Part 2:
1. Turn all values that aren't part of the loop into placeholder values e.g. "."
2. Use the ray-casting algorithm to determine which points are considered 'outside' values, a.k.a values that are not enclosed
3. Take all possible pieces, subtract the number of 'outside' values and loop pieces from that total
"""
