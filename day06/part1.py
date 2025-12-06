from _utils.text_utils import get_lines


def calculate(symbol: str, numbers: list[int]) -> int:
    if symbol == "+":
        return sum(numbers)
    elif symbol == "*":
        result = 1
        for number in numbers:
            result *= number
        return result
    else:
        raise ValueError(f"Unknown symbol: {symbol}")


def get_result_part_1(data: str):
    """Gets the result"""

    lines = get_lines(data)
    symbols = lines[len(lines) - 1].split()

    columns: list[list[int]] = []

    for i in range(0, len(lines) - 1):
        numbers = list(map(int, lines[i].split()))
        for j, number in enumerate(numbers):
            if len(columns) <= j:
                columns.append([])
            columns[j].append(number)

    result = 0
    for i, symbol in enumerate(symbols):
        column = columns[i]
        result += calculate(symbol, column)

    return result
