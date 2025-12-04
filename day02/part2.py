from _utils.text_utils import get_comma_separated


def is_pal(s: str) -> bool:
    l = len(s)

    for i in range(1, l):
        part = s[0:i]
        all = part * (l // i)

        if all == s:
            return True

    return False


def get_result_part_2(data: str):
    """Gets the result"""
    lines = get_comma_separated(data)

    result = 0
    for line in lines:
        parts = line.split("-")

        left = int(parts[0])
        right = int(parts[1])

        for i in range(left, right + 1):
            if is_pal(str(i)):
                result += i

    return result
