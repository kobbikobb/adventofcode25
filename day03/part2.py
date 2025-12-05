from _utils.text_utils import get_lines


def highest_index(line: str):

    highest = int(line[0])
    index = 0

    for i in range(1, len(line)):
        num = int(line[i])

        if num > highest:
            highest = num
            index = i

    return index


def get_jolt(line: str):
    """Get lines"""

    numbs = ""
    curr_index = 0

    for i in range(0, 12):
        part = line[curr_index : len(line) - 11 + i]
        new_index = highest_index(part)
        numbs += part[new_index]
        curr_index = curr_index + new_index + 1

    return int(numbs)


def get_result_part_2(data: str):
    """Gets the restult"""
    lines = get_lines(data)

    result = 0

    for line in lines:

        result += get_jolt(line)

    return result
