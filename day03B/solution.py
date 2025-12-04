def read_input_data(filename):
    """Parse the input file and return the data."""
    with open(filename, 'r') as f:
        return f.read().strip()


def get_lines(data):
    """Get lines"""
    return data.split('\n')


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
        part = line[curr_index:len(line) - 11 + i]
        new_index = highest_index(part)
        numbs += part[new_index]
        curr_index =  curr_index + new_index + 1


    return int(numbs)

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
