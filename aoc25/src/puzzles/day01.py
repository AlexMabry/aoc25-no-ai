from ..utils import parse_data


def parse_rotations(rows):
    directions = []
    for row in rows:
        direction = row[0]
        amount = int(row[1:])

        if direction == "L":
            amount = amount * -1

        directions.append(amount)

    return directions


def solve_part1(data: str):
    input_data = parse_data(data)

    dial = 50
    count = 0

    for turn in parse_rotations(input_data):
        dial = (dial + turn) % 100

        if dial == 0:
            count += 1

    return count


def solve_part2(data: str):
    input_data = parse_data(data)

    dial = 50
    count = 0

    for turn in parse_rotations(input_data):
        prev_dial = dial
        dial = dial + turn

        full_turns = int(dial / 100)
        count += abs(full_turns)

        if dial == 0 or (prev_dial > 0 > dial) or (prev_dial < 0 < dial):
            count += 1

        dial %= 100

    return count
