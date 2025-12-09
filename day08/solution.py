from _utils.text_utils import read_input_data
from day08.part1 import get_result_part_1


def main():
    """The solution"""
    data = read_input_data("input.txt")

    result1 = get_result_part_1(data, 1000)
    print(f"result 1 :{result1}")


if __name__ == "__main__":
    # 1: 244188 Correct
    main()
