from _utils.text_utils import read_input_data
from day06.part1 import get_result_part_1
from day06.part2 import get_result_part_2


def main():
    """The solution"""
    data = read_input_data("input.txt")

    result1 = get_result_part_1(data)
    print(f"result 1 :{result1}")

    result2 = get_result_part_2(data)
    print(f"result 2 :{result2}")


if __name__ == "__main__":
    # 4412382293768 Correct
    # 7858808482092 Correct
    main()
