TEST = False


def read_input():
    filename = "inputs/day03-input.txt"
    if TEST:
        filename = "inputs/day03-test.txt"
    with open(filename, "r", encoding="utf-8") as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
    return lines


def has_symbol_neighbour(x, y, lines):
    gear_neigbours = set()
    has_neighbour = False
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            x0 = x + dx
            y0 = y + dy
            if x0 < 0 or y0 < 0 or x0 >= len(lines) or y0 >= len(lines[0]):
                continue
            neigh = lines[x0][y0]
            if not neigh.isdigit() and neigh != ".":
                has_neighbour = True
                if neigh == "*":
                    gear_neigbours.add((x0, y0))
    return has_neighbour, gear_neigbours


def main():
    lines = read_input()
    total_parts = 0
    gears = {}

    for i, line in enumerate(lines):
        digits = ""
        is_part_number = False
        gear_neigbours = set()
        for j, char in enumerate(line):
            if char.isdigit():
                digits += char
                has_neighbour, digit_gear_neigbours = has_symbol_neighbour(i, j, lines)
                is_part_number |= has_neighbour
                gear_neigbours |= digit_gear_neigbours
            if not char.isdigit() or j == len(line) - 1:
                if digits and is_part_number:
                    number = int(digits)
                    total_parts += number
                    if gear_neigbours:
                        for gx, gy in gear_neigbours:
                            gears.setdefault((gx, gy), []).append(number)
                is_part_number = False
                gear_neigbours = set()
                digits = ""
    print(total_parts)

    total_ratio = 0
    for gear, numbers in gears.items():
        if len(numbers) == 2:
            total_ratio += numbers[0] * numbers[1]
    print(total_ratio)


if __name__ == "__main__":
    main()
