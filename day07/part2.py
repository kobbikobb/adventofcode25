from os import wait
from functools import lru_cache
from _utils.text_utils import get_lines

def sum_routes(lines: list[str], row: int, col: int) -> int:
    @lru_cache(None)
    def walk(r: int, c: int) -> int:
        if r + 2 > len(lines):
            return 1

        cell = lines[r][c]

        if cell == "^":
            total = 0
            if c > 0:
                total += walk(r + 2, c - 1)
            if c < len(lines[r]) - 1:
                total += walk(r + 2, c + 1)
            return total
        else:
            return walk(r + 2, c)

    return walk(row, col)

def get_result_part_2(data: str):
    """Gets the result"""

    lines = get_lines(data)
    first = lines[0].index("S")

    total: int = sum_routes(lines, 2, first)

    return total
