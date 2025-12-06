from _utils.text_utils import get_lines


def get_index_empty_line(lines: list[str]) -> int:
    for i, line in enumerate(lines):
        if line.strip() == "":
            return i
    raise ValueError("No empty line found")


def sum_tuple(t: tuple[int, int]) -> int:
    left, right = t
    return right - left + 1

def get_result_part_2(data: str):
    """Gets the result"""

    lines = get_lines(data)
    emtpy_line_index = get_index_empty_line(lines)

    ranges = lines[:emtpy_line_index]

    intervals: list[tuple[int, int]] = []
    for r in ranges:
        left, right = map(int, r.split("-"))
        intervals.append((left, right))

    intervals.sort(key=lambda x: x[0])

    uniques: list[tuple[int, int]] = list()
    uniques.append(intervals[0])

    for i in range(1, len(intervals)):
        left, right = intervals[i]
        last_left, last_right = uniques[-1]

        if left > last_right:
            uniques.append((left, right))
        else:
            uniques[-1] = (last_left, max(last_right, right))

    return sum(sum_tuple(t) for t in uniques)
