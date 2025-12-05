from _utils.text_utils import get_lines


def get_jolt(line: str):
    """Get lines"""

    # Find the highest number that is not last
    highest1 = int(line[0])
    index = 0
    for i in range(1, len(line) - 1):
        num = int(line[i])

        if num > highest1:
            highest1 = num
            index = i

    # Find the next highest after that
    highest2 = int(line[(index + 1) % len(line)])
    for i in range(index + 1, len(line)):
        num = int(line[i])

        if num > highest2:
            highest2 = num
            index = i

    return int(f"{highest1}{highest2}")


def get_result_part_1(data: str):
    """Gets the result"""
    lines = get_lines(data)

    result = 0

    for line in lines:

        result += get_jolt(line)

    return result
