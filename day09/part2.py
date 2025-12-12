from _utils.text_utils import get_lines


def size_between_corners(corner_a: tuple[int, int], corner_b: tuple[int, int]) -> int:
    """Calculates the size between two corners"""

    size_x = abs(corner_a[0] - corner_b[0]) + 1
    size_y = abs(corner_a[1] - corner_b[1]) + 1

    return size_x * size_y


def compute_green_ranges(
    red_corners: list[tuple[int, int]],
) -> dict[int, tuple[int, int]]:
    """Computes covered x-ranges for each y-coordinate (more memory efficient than storing every cell)"""

    covered: set[tuple[int, int]] = set()

    for x, y in red_corners:
        covered.add((x, y))

    # Add green segments between corners
    for i, (x, y) in enumerate(red_corners):
        xn, yn = red_corners[(i + 1) % len(red_corners)]

        if x == xn and abs(y - yn) > 1:
            for yy in range(min(y, yn) + 1, max(y, yn)):
                covered.add((x, yy))
        elif y == yn and abs(x - xn) > 1:
            for xx in range(min(x, xn) + 1, max(x, xn)):
                covered.add((xx, y))

    # Convert to ranges
    ranges: dict[int, tuple[int, int]] = {}
    min_y = min(y for _, y in covered)
    max_y = max(y for _, y in covered)

    for y in range(min_y, max_y + 1):
        xs_at_y = [x for x, yy in covered if yy == y]
        if len(xs_at_y) >= 2:
            # interior fill: everything between leftmost and rightmost is covered
            ranges[y] = (min(xs_at_y), max(xs_at_y))
        elif len(xs_at_y) == 1:
            # single point on this row
            new_x = xs_at_y[0]
            ranges[y] = (new_x, new_x)

    return ranges


def is_full(
    corner_a: tuple[int, int],
    corner_b: tuple[int, int],
    covered_ranges: dict[int, tuple[int, int]],
) -> bool:
    """check if all cells in rectangle (except corners) are covered using ranges"""
    rect_x_min = min(corner_a[0], corner_b[0])
    rect_x_max = max(corner_a[0], corner_b[0])
    rect_y_min = min(corner_a[1], corner_b[1])
    rect_y_max = max(corner_a[1], corner_b[1])

    for y in range(rect_y_min, rect_y_max):
        # check if this row exists in covered ranges
        if y not in covered_ranges:
            return False

        covered_x_min, covered_x_max = covered_ranges[y]

        # check if the covered range fully contains the rectangle's x-range for this row
        if covered_x_min > rect_x_min or covered_x_max < rect_x_max:
            return False

    return True


def find_biggest_rectangle(
    corners: list[tuple[int, int]], covered_ranges: dict[int, tuple[int, int]]
) -> int:
    """Finds the biggest rectangle that is fully covered"""
    result = 0

    for corner_a in corners:
        for corner_b in corners:
            if corner_a == corner_b:
                continue

            if not is_full(corner_a, corner_b, covered_ranges):
                continue

            size = size_between_corners(corner_a, corner_b)
            result = max(result, size)

    return result


def get_result_part_2(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)

    red_corners: list[tuple[int, int]] = [
        (int(a), int(b)) for a, b in (line.split(",") for line in lines)
    ]

    covered_ranges = compute_green_ranges(red_corners)

    print("covered_ranges")
    return find_biggest_rectangle(red_corners, covered_ranges)
