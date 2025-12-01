def parse_input(filename):
    """Parse the input file and return the data."""
    with open(filename, 'r') as f:
        return f.read().strip()


def part1(data):
    """Solve part 1: Count the number of lines."""
    lines = data.split('\n')
    return len(lines)


def part2(data):
    """Solve part 2: Sum all numbers in the input."""
    total = 0
    for line in data.split('\n'):
        try:
            total += int(line)
        except ValueError:
            pass
    return total


def main():
    """Main function to run both parts."""
    data = parse_input("input.txt")

    result1 = part1(data)
    result2 = part2(data)

    print("Part 1:", result1)
    print("Part 2:", result2)

    return result1, result2


if __name__ == "__main__":
    main()
