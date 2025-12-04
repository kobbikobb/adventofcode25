from _utils.text_utils import get_lines, read_input_data


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


def get_hits_part_2(data: str):
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


def main():
    """Run day"""
    data = read_input_data("input.txt")

    hits_1 = get_hits_part_1(data)
    print(f"hits 1 = {hits_1}")

    hits_2 = get_hits_part_2(data)
    print(f"hits 2 = {hits_2}")


if __name__ == "__main__":
    # 1018 Correct
    main()
