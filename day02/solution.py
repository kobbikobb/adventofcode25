def read_input_data(filename):
    """Parse the input file and return the data."""
    with open(filename, "r") as f:
        return f.read().strip()


def get_ranges(data):
    """Get lines"""
    return data.split(",")


def is_pal(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]

    for i in range(mid):
        if left[i] != right[i]:
            return False

    return True


def do_it(data):
    """Gets the hit"""
    lines = get_ranges(data)

    sum = 0
    for line in lines:
        print(line)
        parts = line.split("-")

        left = int(parts[0])
        right = int(parts[1])

        for i in range(left, right + 1):
            if is_pal(str(i)):
                sum += i

    return sum


def main():
    """The solution"""
    data = read_input_data("input.txt")
    result = do_it(data)

    print(f"result {result}")


if __name__ == "__main__":
    # 1018 Correct
    main()
