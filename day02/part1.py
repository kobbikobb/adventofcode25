from _utils.text_utils import get_comma_separated


def is_pal(s: str) -> bool:
    """Checks if the string is a palindrome"""
    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]

    for i in range(mid):
        if left[i] != right[i]:
            return False

    return True


def get_result_part_1(data: str):
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
