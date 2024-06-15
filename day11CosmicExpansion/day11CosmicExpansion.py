grid = open(0).read().splitlines()

galaxy_coords = []
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "#":
            galaxy_coords.append((r, c))

empty_rows = set()
for i, row in enumerate(grid):
    if all(char == "." for char in row):
        empty_rows.add(i)

empty_cols = set()
for i, col in enumerate(zip(*grid)):
    if all(char == "." for char in col):
        empty_cols.add(i)

coord_pairs = []
for i in range(len(galaxy_coords)):
    for j in range(i + 1, len(galaxy_coords)):
        coord_pairs.append((galaxy_coords[i], galaxy_coords[j]))


def calculate_dist(
    coord1: tuple[int, int],
    coord2: tuple[int, int],
    empty_rows: set[int],
    empty_cols: set[int],
) -> int:
    sum = 0
    start_row = min(coord1[0], coord2[0])
    end_row = max(coord1[0], coord2[0])
    start_col = min(coord1[1], coord2[1])
    end_col = max(coord1[1], coord2[1])

    for i in range(start_row, end_row):
        if i in empty_rows:
            sum += 2
        else:
            sum += 1

    for j in range(start_col, end_col):
        if j in empty_cols:
            sum += 2
        else:
            sum += 1

    return sum


total_sum = 0
for coord1, coord2 in coord_pairs:
    total_sum += calculate_dist(coord1, coord2, empty_rows, empty_cols)

print(total_sum)


"""
Approach:
1. Collect all galaxy coordinates
2. Collect empty row and column indices 
3. Collect all pairs of galaxys
4. Calculate num steps between all pairs, counting steps as 2 for each time it crosses an empty row/column
"""
