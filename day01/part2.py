from _utils.text_utils import get_lines


def get_hits_part_2(data: str):
    """Gets the hit"""
    lines = get_lines(data)

    start = 50
    hit = 0

    for line in lines:
        digit = line[0]
        number = int(line[1:])

        if digit == "L":
            org = start
            start = start - number
            if start < 0:
                hit = hit + abs(start) // 100
                if org != 0:
                    hit = hit + 1

                start = 100 + start
            elif start == 0:
                hit = hit + 1
        elif digit == "R":
            start = start + number
            if start > 99:
                hit = hit + abs(start) // 100

                start = start - 100
        else:
            raise Exception("Illegal input")

        start = start % 100

    return hit
