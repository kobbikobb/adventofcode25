import math


def read_input_data(filename):
    """Parse the input file and return the data."""
    with open(filename, 'r') as f:
        return f.read().strip()


def get_lines(data):
    """Get lines"""
    return data.split('\n')

def get_hit(data):
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
                hit = hit + math.floor(abs(start) / 100)
                if org != 0:
                    hit = hit + 1

                start = (100 + start)
            elif start == 0:
                hit = hit + 1
        elif digit == "R":
            start = (start + number)
            if start > 99:
                hit = hit + math.floor(abs(start) / 100)

                start = (start - 100)
        else:
            raise Exception("Illegal input")

        start = start % 100

        print(start)

    return hit

def main():
    """The solution"""
    data = read_input_data("input.txt")
    hit = get_hit(data)

    print(f"hits {hit}")

if __name__ == "__main__":
    # 5815 Correct
    main()
