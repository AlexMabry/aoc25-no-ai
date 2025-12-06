from ..utils import parse_data

Locations = set[tuple[int, int]]


def get_rolls(data: str) -> Locations:
    grid = parse_data(data)
    return {(x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c == "@"}


def get_neighbors(x: int, y: int) -> Locations:
    close = [-1, 0, 1]
    return {(x + dx, y + dy) for dx in close for dy in close if dx != 0 or dy != 0}


def rolls_to_remove(rolls: Locations) -> Locations:
    return {roll for roll in rolls if len(get_neighbors(*roll) & rolls) < 4}


def solve_part1(data: str):
    rolls = get_rolls(data)
    to_remove = rolls_to_remove(rolls)

    return len(to_remove)


def solve_part2(data: str):
    rolls = get_rolls(data)
    to_remove = rolls_to_remove(rolls)
    removed = set()

    while to_remove:
        rolls = rolls - to_remove
        removed = removed | to_remove
        to_remove = rolls_to_remove(rolls)

    return len(removed)
