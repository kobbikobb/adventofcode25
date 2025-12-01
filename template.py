def parse_input(filename):
    """Parse the input file and return the data."""
    with open(filename, 'r') as f:
        return f.read().strip()


def part1(data):
    """Solve part 1 of the puzzle."""
    pass


def part2(data):
    """Solve part 2 of the puzzle."""
    pass


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
