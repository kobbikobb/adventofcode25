from _utils.text_utils import get_lines


def size_between_corners(corner_a: tuple[int, int], corner_b: tuple[int, int]) -> int:
    """Calculates the size between two corners"""

    size_x = abs(corner_a[0] - corner_b[0]) + 1
    size_y = abs(corner_a[1] - corner_b[1]) + 1

    return size_x * size_y


def print_grid(grid: list[list[str]]) -> None:
    """Prints the grid"""

    for row in grid:
        print("".join(row))
    print()


def populate_grid(corners: list[tuple[int, int]], grid: list[list[str]]):
    for i, corner in enumerate(corners):

        x, y = corner
        grid[y][x] = "#"

        index = (i + 1) % (len(corners))
        xn, yn = corners[index]

        if x == xn and abs(y - yn) > 1:
            for yy in range(min(y, yn) + 1, max(y, yn)):
                grid[yy][x] = "X"

        if y == yn and abs(x - xn) > 1:
            for xx in range(min(x, xn) + 1, max(x, xn)):
                grid[y][xx] = "X"

    for row in grid:

        line = "".join(row)
        if "X" not in line:
            continue
        first = line.index("X")
        last = line.rindex("X")

        for i in range(first, last):
            if row[i] == "#":
                continue
            row[i] = "X"


def is_full(
    corner_a: tuple[int, int], corner_b: tuple[int, int], grid: list[list[str]]
):

    for y in range(min(corner_a[1], corner_b[1]), max(corner_a[1], corner_b[1])):
        for x in range(min(corner_a[0], corner_b[0]), max(corner_a[0], corner_b[0])):
            if x == corner_a[0] and y == corner_a[1]:
                continue
            if x == corner_b[0] and y == corner_b[1]:
                continue
            if grid[y][x] == ".":
                return False
    return True


def find_biggest(corners: list[tuple[int, int]], grid: list[list[str]]):
    result = 0

    for i, corner_a in enumerate(corners):
        print(f"{i} of {len(corners)}")
        for corner_b in corners:
            if corner_a == corner_b:
                continue

            if not is_full(corner_a, corner_b, grid):
                continue

            size = size_between_corners(corner_a, corner_b)
            result = max(result, size)

    return result


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)

    corners: list[tuple[int, int]] = [
        (int(a), int(b)) for a, b in (line.split(",") for line in lines)
    ]

    max_x = max(corner[0] for corner in corners)
    max_y = max(corner[1] for corner in corners)

    grid: list[list[str]] = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    populate_grid(corners, grid)
    print_grid(grid)

    return find_biggest(corners, grid)
