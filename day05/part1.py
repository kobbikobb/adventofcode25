from _utils.text_utils import get_lines


def get_index_empty_line(lines: list[str]) -> int:
    for i, line in enumerate(lines):
        if line.strip() == "":
            return i
    raise ValueError("No empty line found")


def is_fresh(number: int, ranges: list[str]) -> bool:
    for rang in ranges:
        range_parts = rang.split("-")
        start = int(range_parts[0])
        end = int(range_parts[1])

        if start <= int(number) <= end:
            return True
    return False


def get_result_part_1(data: str):
    """Gets the result"""

    lines = get_lines(data)
    emtpy_line_index = get_index_empty_line(lines)

    ranges = lines[:emtpy_line_index]
    numbers = lines[emtpy_line_index + 1 :]

    result = 0

    for number in numbers:
        if is_fresh(int(number), ranges):
            result += 1

    return result
