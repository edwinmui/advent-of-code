
def cube(inp):
    cube_color_dict = {"red": 12, "green": 13, "blue": 14}

    running_sum = 0

    for i in range(len(inp)):
        flag = True
        line = inp[i].strip().split(":")
        stripped_line = line[1]
        hands = stripped_line.strip().split(";")
        for hand in hands:
            cubes = hand.strip().split(",")
            for cube in cubes:
                number = int(cube[0].strip())
                color = cube[1 : len(cube)].strip()
                if number > cube_color_dict[color]:
                    flag = False
        if flag:
            running_sum += i + 1

    return running_sum


def main():
    file1 = open("day2Cube.txt", "r")
    inp = list(file1)
    for i in range(len(inp)):
        inp[i] = inp[i].strip()
    print(cube(inp))


if __name__ == "__main__":
    main()
