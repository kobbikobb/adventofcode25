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
            start = start - number
            if start < 0:
                start = (100 + start) % 100
        elif digit == "R":
            start = (start + number)
            if start > 99:
                start = (start - 100) % 100
        else:
            raise Exception("Illegal input")

        print(start)

        if start == 0:
            hit = hit + 1

    return hit

def main():
    """The solution"""
    data = read_input_data("input.txt")
    hit = get_hit(data)

    print(f"hits {hit}")

if __name__ == "__main__":
    # 1018 Correct
    main()
