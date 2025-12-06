from ..utils import parse_data


def joltage(bank: list, length: int) -> int:
    if length == 1:
        return max(bank)

    next_range = bank[: -(length - 1)]
    first_digit = max(set(next_range))

    highest_value = 0
    for ix, battery in enumerate(next_range):
        if battery == first_digit:
            possible_following = joltage(bank[ix + 1 :], length - 1)
            highest_value = max(highest_value, possible_following)

    return int(str(first_digit) + str(highest_value))


def solve_part1(data: str):
    banks = [[int(c) for c in row] for row in parse_data(data)]
    return sum(joltage(bank, 2) for bank in banks)


def solve_part2(data: str):
    banks = [[int(c) for c in row] for row in parse_data(data)]
    return sum(joltage(bank, 12) for bank in banks)
