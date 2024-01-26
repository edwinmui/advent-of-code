games = open(0).read().strip().splitlines()

cube_color_dict = {"red": 12, "green": 13, "blue": 14}

running_sum = 0

for game in games:
    id_and_game = game.split(":")
    game_id = int(id_and_game[0].split()[1])
    game = id_and_game[1].strip()

    hands = game.split(";")

    flag = True
    for hand in hands:
        marbles = hand.split(",")
        for marble_group in marbles:
            number_and_color = marble_group.strip().split()
            number = int(number_and_color[0].strip())
            color = number_and_color[1].strip()

            if number > cube_color_dict[color]:
                flag = False
                break
        else:
            continue
        break

    if flag:
        running_sum += game_id

print(running_sum)
# def cube(games):
#     cube_color_dict = {"red": 12, "green": 13, "blue": 14}

#     running_sum = 0

#     for game in games:
#         id_and_game = game.split(":")
#         game_id = int(id_and_game[0].split()[1])
#         game = id_and_game[1].strip()

#         hands = game.split(";")

#         flag = True
#         for hand in hands:
#             marbles = hand.split(",")
#             for marble_group in marbles:
#                 # breakpoint()
#                 number_and_color = marble_group.strip().split()
#                 number = int(number_and_color[0].strip())
#                 color = number_and_color[1].strip()

#                 if number > cube_color_dict[color]:
#                     flag = False
#                     break
#             else:
#                 continue
#             break
    
#         if flag:
#             running_sum += game_id

#     print(running_sum)


# def main():
#     file1 = open("day2Cube.txt", "r").readlines()
#     cube(file1)


# if __name__ == "__main__":
#     main()
