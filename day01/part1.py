from _utils.text_utils import get_lines


def get_hits_part_1(data: str):
    """Gets the hit"""
    lines = get_lines(data)

    start = 50
    hit = 0

    for line in lines:
        digit = line[0]
        number = int(line[1:])

        if digit == "L":
            start = start - number
            if start < 0:
                start = (100 + start) % 100
        elif digit == "R":
            start = start + number
            if start > 99:
                start = (start - 100) % 100
        else:
            raise Exception("Illegal input")

        if start == 0:
            hit = hit + 1

    return hit
