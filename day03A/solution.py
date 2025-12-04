def read_input_data(filename):
    """Parse the input file and return the data."""
    with open(filename, 'r') as f:
        return f.read().strip()


def get_lines(data):
    """Get lines"""
    return data.split('\n')

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

    print(index)
    print(f"{highest1}{highest2}")

    return int(f"{highest1}{highest2}")

def get_solution(data):
    """Gets the hit"""
    lines = get_lines(data)

    sum = 0

    for line in lines:

        sum += get_jolt(line)

    return sum

def main():
    """The solution"""
    data = read_input_data("input.txt")
    solution = get_solution(data)

    print(f"solution {solution}")

if __name__ == "__main__":
    # 17158
    main()
