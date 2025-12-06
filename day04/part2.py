from _utils.text_utils import get_lines


def is_paper(char: str):
    return char == "@" or char == "x"

def is_hit(prev: str | None, curr: str, nxt: str | None, index: int) -> bool:
    """Checks if there is a hit at the given index"""

    c = curr[index]
    if c != "@":
        return False

    count = 0
    if index > 0:
        if is_paper(curr[index - 1]):
            count += 1
        if prev and is_paper(prev[index - 1]):
            count += 1
        if nxt and is_paper(nxt[index - 1]):
            count += 1

    if prev and is_paper(prev[index]):
        count += 1
    if nxt and is_paper(nxt[index]):
        count += 1

    if index + 1 < len(curr):
        if is_paper(curr[index + 1]):
            count += 1
        if prev and is_paper(prev[index + 1]):
            count += 1
        if nxt and is_paper(nxt[index + 1]):
            count += 1

    return count < 4

def get_result_from_lines(lines: list[str], result):
    """Gets the result"""

    cols = len(lines[0])

    org = result

    for i in range(len(lines)):

        prev = lines[i - 1] if i - 1 >= 0 else None
        curr = lines[i]
        nxt = lines[i + 1] if i + 1 < len(lines) else None

        for j in range(cols):
            if is_hit(prev, curr, nxt, j):
                result += 1
                curr = curr[:j] + "x" + curr[j + 1:]
                lines[i] = curr

    if org == result:
        return result

    for i in range(len(lines)):
        lines[i] = lines[i].replace("x", ".")

    return get_result_from_lines(lines, result)

def get_result_part_2(data: str):
    """Gets the result"""
    lines = get_lines(data)

    return get_result_from_lines(lines, 0)
