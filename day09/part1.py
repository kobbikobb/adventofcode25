from _utils.text_utils import get_lines


def size_between_corners(corner_a: tuple[int, int], corner_b: tuple[int, int]) -> int:
    """Calculates the size between two corners"""

    size_x = abs(corner_a[0] - corner_b[0]) + 1
    size_y = abs(corner_a[1] - corner_b[1]) + 1

    return size_x * size_y


def get_result_part_1(data: str) -> int:
    """Gets the result"""

    lines: list[str] = get_lines(data)
    corners: list[tuple[int, int]] = [
        (int(a), int(b)) for a, b in (line.split(",") for line in lines)
    ]

    result = 0

    for corner_a in corners:

        for corner_b in corners:

            if corner_a == corner_b:
                continue

            size = size_between_corners(corner_a, corner_b)
            result = max(result, size)

    return result
