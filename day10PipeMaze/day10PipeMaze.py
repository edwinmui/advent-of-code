from typing import List, Union

pipe_connections = {
    "|": {
        "up": ["|", "7", "F"],
        "right": [],
        "down": ["|", "L", "J"],
        "left": [],
    },
    "-": {
        "up": [],
        "right": ["-", "J", "7"],
        "down": [],
        "left": ["-", "L", "F"],
    },
    "L": {
        "up": ["|", "7", "F"],
        "right": ["-", "J", "7"],
        "down": [],
        "left": [],
    },
    "J": {
        "up": ["|", "7", "F"],
        "right": [],
        "down": [],
        "left": ["-", "L", "F"],
    },
    "7": {
        "up": [],
        "right": [],
        "down": ["|", "L", "J"],
        "left": ["-", "L", "F"],
    },
    "F": {
        "up": [],
        "right": ["-", "J", "7"],
        "down": ["|", "L", "J"],
        "left": [],
    }
}

def find_S(grid: List[List[str]]) -> Union[List[int], None]:
    N = len(grid)
    M = len(grid[0])
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "S":
                return [i, j]
    
    return None

def pipeMaze(grid):
    row_col = find_S(grid)
    row = row_col[0]
    col = row_col[1]

    return row_col
    

def main():
    file1 = open("day10PipeMaze.txt", "r")
    file_contents = file1.readlines()
    print(pipeMaze(file_contents))


if __name__ == "__main__":
    main()


