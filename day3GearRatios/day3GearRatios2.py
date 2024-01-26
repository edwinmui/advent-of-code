grid = open(0).read().strip().splitlines()
N = len(grid)
M = len(grid[0])

visited = [[False for _ in range(M)] for _ in range(N)]

def is_valid_move(r, c, num_grid_rows, num_grid_cols):
    if r < 0 or r >= num_grid_rows or c < 0 or c >= num_grid_cols:
        return False
    return True

def locate_part_number(new_r, new_c, grid, visited):
    l = new_c
    r = new_c
    while (is_valid_move(new_r, l - 1, N, M) and grid[new_r][l - 1].isnumeric()):
        l -= 1
    while (is_valid_move(new_r, r + 1, N, M) and grid[new_r][r + 1].isnumeric()):
        r += 1
    part_number = int(grid[new_r][l : r + 1])
    while (l <= r):
        visited[new_r][l] = True
        l += 1
    return part_number

def append_gear_ratio_if_exists(r, c, grid, gear_ratios, visited):
    possible_moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    part_numbers = []
    for move in possible_moves:
        new_r = r + move[0]
        new_c = c + move[1]
        if not is_valid_move(new_r, new_c, N, M) or visited[new_r][new_c]:
            continue
        if grid[new_r][new_c].isnumeric():
            part_numbers.append(locate_part_number(new_r, new_c, grid, visited))
    
    if len(part_numbers) == 2:
        gear_ratios.append(part_numbers[0] * part_numbers[1])
    visited = [[False for _ in range(M)] for _ in range(N)]


gear_ratios = []
for r in range(N):
    for c in range(M):
        if grid[r][c] == '*':
            append_gear_ratio_if_exists(r, c, grid, gear_ratios, visited)

total_sum = 0
for num in gear_ratios:
    total_sum += num

print(total_sum)