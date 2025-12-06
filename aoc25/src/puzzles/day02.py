from itertools import batched

from ..utils import parse_data


def parse_ranges(data: str):
    input_data = "".join(parse_data(data)).split(",")

    ranges = []
    for row in input_data:
        parts = row.split("-")
        id_range = range(int(parts[0]), int(parts[1]) + 2)
        ranges.append(id_range)

    return ranges


def spilt_string(str_num: str, parts: int) -> set[str]:
    if parts and len(str_num) % parts == 0:
        return {"".join(b) for b in batched(str_num, parts)}

    return set()


def solve_part1(data: str):
    answer = 0

    for id_range in parse_ranges(data):
        for number in id_range:
            str_number = str(number)
            sequences = spilt_string(str_number, len(str_number) // 2)
            if len(sequences) == 1:
                answer += number

    return answer


def solve_part2(data: str):
    answer = 0

    for id_range in parse_ranges(data):
        for number in id_range:
            str_number = str(number)
            for window in range(len(str_number) // 2):
                sequences = spilt_string(str_number, window + 1)
                if len(sequences) == 1:
                    answer += number
                    break

    return answer
