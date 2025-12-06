from itertools import zip_longest

from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)
    problems = [row.split() for row in input_data]
    statements = (f" {p[-1]} ".join(p[:-1]) for p in zip(*problems))

    return sum(map(eval, statements))


def solve_part2(data: str):
    input_data = parse_data(data)

    answer = 0
    numbers = []
    for column in zip_longest(*map(reversed, input_data), fillvalue=""):
        value = "".join(column[:-1]).strip()
        if value:
            numbers.append(value)

        operator = column[-1].strip()
        if operator:
            answer += eval(f" {operator} ".join(numbers))
            numbers = []

    return answer
