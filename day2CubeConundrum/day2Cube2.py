games = open(0).read().strip().splitlines()

running_power_sum = 0

for game in games:
    game_min_cube_dict = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    id_and_game = game.split(":")
    game_id = int(id_and_game[0].split()[1])
    game = id_and_game[1].strip()

    hands = game.split(";")

    for hand in hands:
        marble_groups = hand.split(",")
        for marble_group in marble_groups:
            number_and_color = marble_group.strip().split()
            number = int(number_and_color[0].strip())
            color = number_and_color[1].strip()

            game_min_cube_dict[color] = max(number, game_min_cube_dict[color])
    
    power = 1
    for val in game_min_cube_dict.values():
        power *= val

    running_power_sum += power

print(running_power_sum)

"""
create a dict of min cubes of a game
iterate through each hand, and each set of marbles, and check how many marbles of a color were pulled
compare color and number of marbles with min-cubes-dict
    set color:marble pair in min-cubes-dict to max(curr_color_and_number, min-cubes_dict[color])
iterate through keys in min-cubes-dict, mulitply them together to receive power
add each power to a running power-sum
return running power-sum
"""
