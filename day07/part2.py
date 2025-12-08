from _utils.text_utils import get_lines

def sum_routes(lines: list[str], row: int, col: int, memo: dict) -> int:
    key = (row, col)
    if key in memo:
        return memo[key]

    if row + 2 > len(lines):
        memo[key] = 1
        return 1

    if lines[row][col] == "^":
        total = 0
        if col > 0:
            total += sum_routes(lines, row + 2, col - 1, memo)
        if col < len(lines[row]) - 1:
            total += sum_routes(lines, row + 2, col + 1, memo)
    else:
        total = sum_routes(lines, row + 2, col, memo)

    memo[key] = total
    return total

def get_result_part_2(data: str):
    """Gets the result"""

    lines = get_lines(data)
    first = lines[0].index("S")

    total: int = sum_routes(lines, 2, first, {})

    return total
