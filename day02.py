from math import prod

TEST = False


def read_input():
    filename = "inputs/day02-input.txt"
    if TEST:
        filename = "inputs/day02-test.txt"
    with open(filename, "r", encoding="utf-8") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
    games = []
    for line in lines:
        _, game = tuple(line.split(": "))
        cube_sets = game.split("; ")
        game = []
        for cube_set in cube_sets:
            cubes = {}
            for cube in cube_set.split(", "):
                number, colour = cube.split(" ")
                cubes[colour] = int(number)
            game.append(cubes)
        games.append(game)
    return games


def get_possible_games(games, max_counts):
    possible_games = []
    for i, game in enumerate(games):
        game_id = i + 1
        game_possible = True
        for cube_set in game:
            for colour, number in cube_set.items():
                if number > max_counts[colour]:
                    game_possible = False
                    break
            if not game_possible:
                break
        if game_possible:
            possible_games.append(game_id)
    return possible_games


def get_game_powers(games):
    powers = []
    for game in games:
        max_counts = {"red": 0, "green": 0, "blue": 0}
        for cube_set in game:
            for colour, number in cube_set.items():
                max_counts[colour] = max([max_counts[colour], number])
        powers.append(prod(max_counts.values()))
    return powers


def main():
    games = read_input()
    max_counts = {"red": 12, "green": 13, "blue": 14}
    possible_games = get_possible_games(games, max_counts)
    print(sum(possible_games))

    powers = get_game_powers(games)
    print(sum(powers))


if __name__ == "__main__":
    main()
