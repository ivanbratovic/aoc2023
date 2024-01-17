test = False


def read_input():
    global test
    filename = "inputs/day01-input.txt"
    if test:
        filename = "inputs/day01-test.txt"
    with open(filename, "r") as file:
        return file.readlines()


def firstlast_line_digits(line, spelling=False):
    words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    digits = []
    for i, char in enumerate(line):
        if char.isdigit():
            digits.append(int(char))
            continue
        if not spelling:
            continue
        for j in range(i, min((len(line)+1, i + 6))):
            substr = line[i:j]
            if substr in words:
                digits.append(words[substr])
                break
    return digits[0], digits[-1]


def get_calibrations(spelling=False):
    values = []
    for line in read_input():
        line = line.strip()
        first, last = firstlast_line_digits(line, spelling)
        values.append(10 * first + last)
    return values


def main():
    print(sum(get_calibrations()))
    print(sum(get_calibrations(spelling=True)))


if __name__ == "__main__":
    main()
