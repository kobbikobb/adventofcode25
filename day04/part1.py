from _utils.text_utils import get_lines


def is_hit(prev: str | None, curr: str, nxt: str | None, index: int) -> bool:
    """Checks if there is a hit at the given index"""

    c = curr[index]
    if c != "@":
        return False

    count = 0
    if index > 0:
        if curr[index - 1] == "@":
            count += 1
        if prev and prev[index - 1] == "@":
            count += 1
        if nxt and nxt[index - 1] == "@":
            count += 1

    if prev and prev[index] == "@":
        count += 1
    if nxt and nxt[index] == "@":
        count += 1

    if index + 1 < len(curr):
        if curr[index + 1] == "@":
            count += 1
        if prev and prev[index + 1] == "@":
            count += 1
        if nxt and nxt[index + 1] == "@":
            count += 1

    return count < 4


def get_result_part_1(data: str):
    """Gets the result"""
    lines = get_lines(data)
    cols = len(lines[0])

    result = 0

    for i in range(len(lines)):

        prev = lines[i - 1] if i - 1 >= 0 else None
        curr = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else None

        for j in range(cols):
            if is_hit(prev, curr, nxt, j):
                result += 1

    return result
