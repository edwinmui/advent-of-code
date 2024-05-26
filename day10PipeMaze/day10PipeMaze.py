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
seen = set()

seen.add((sr, sc))
q.append((sr, sc))

while q:
    cr, cc = q.popleft()
    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)

    # Up
    ur, uc = cr + up[0], cc + up[1]
    if (
        (ur, uc) not in seen
        and is_allowed(ur, uc)
        and grid[cr][cc] in "S|LJ"
        and grid[ur][uc] in "|7F"
    ):
        seen.add((ur, uc))
        q.append((ur, uc))

    # Right
    rr, rc = cr + right[0], cc + right[1]
    if (
        (rr, rc) not in seen
        and is_allowed(rr, rc)
        and grid[cr][cc] in "S-LF"
        and grid[rr][rc] in "-J7"
    ):
        seen.add((rr, rc))
        q.append((rr, rc))

    # Down
    dr, dc = cr + down[0], cc + down[1]
    if (
        (dr, dc) not in seen
        and is_allowed(dr, dc)
        and grid[cr][cc] in "S|7F"
        and grid[dr][dc] in "|LJ"
    ):
        seen.add((dr, dc))
        q.append((dr, dc))

    # Left
    lr, lc = cr + left[0], cc + left[1]
    if (
        (lr, lc) not in seen
        and is_allowed(lr, lc)
        and grid[cr][cc] in "S-J7"
        and grid[lr][lc] in "-LF"
    ):
        seen.add((lr, lc))
        q.append((lr, lc))

print(len(seen) // 2)


"""
|-LJ7F
For each direction (e.g. up), check:
0. If coordinate above is not in seen
1. If allowed to move in that direction
2. If current piece allows to go in that direction
3. If piece above allows to go in that direction
"""
