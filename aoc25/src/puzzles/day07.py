from ..utils import parse_data


def solve_part1(data: str):
    rows = parse_data(data)

    splits = 0
    last_beams = {(rows[0].find("S"), 1)}
    for iy, row in enumerate(rows[2:], start=2):
        curr_beams = set()
        for ix, c in enumerate(row):
            if (ix, iy - 1) in last_beams:
                if c == "^":
                    splits += 1
                    curr_beams |= {(ix - 1, iy), (ix + 1, iy)}
                else:
                    curr_beams.add((ix, iy))
        last_beams = curr_beams

    return splits


def solve_part2(data: str):
    input_data = parse_data(data)
    print(input_data)

    return None
