from typing import Iterator

from ..utils import parse_data


def get_fresh_id_ranges(rows: Iterator[str]) -> list[tuple[int, int]]:
    ranges = []

    # stops when it hits a blank line
    while row := next(rows):
        ranges.append(tuple(map(int, row.split("-"))))

    return ranges


def solve_part1(data: str):
    input_data = iter(parse_data(data))  # iter allows further processing
    ranges = get_fresh_id_ranges(input_data)

    count = 0
    for row in input_data:
        for id_range in ranges:
            if id_range[0] <= int(row) <= id_range[1]:
                count += 1
                break

    return count


def combine_ranges(ranges: list) -> list:
    new_ranges = []
    combined = []
    sorted_ranges = list(sorted(ranges))

    for ix, a_range in enumerate(sorted_ranges):
        if a_range not in combined:
            for b_range in sorted_ranges[ix + 1 :]:
                if b_range not in combined and a_range[0] <= b_range[0] <= a_range[1]:
                    new_ranges.append((a_range[0], max(a_range[1], b_range[1])))
                    combined.extend([a_range, b_range])
                    break

            if a_range not in combined:
                new_ranges.append(a_range)
                combined.append(a_range)

    return new_ranges


def solve_part2(data: str):
    input_data = iter(parse_data(data))
    ranges = get_fresh_id_ranges(input_data)

    while (new_ranges := combine_ranges(ranges)) != ranges:
        ranges = new_ranges

    return sum((id_range[1] - id_range[0] + 1) for id_range in ranges)
