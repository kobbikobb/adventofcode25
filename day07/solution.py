from _utils.text_utils import read_input_data
from day07.part1 import get_result_part_1
from day07.part2 import get_result_part_2

def main():
    """The solution"""
    data = read_input_data("input.txt")

    result1 = get_result_part_1(data)
    print(f"result 1 :{result1}")

    result2 = get_result_part_2(data)
    print(f"result 2 :{result2}")

if __name__ == "__main__":
    # 863 TOO LOW
    # 1587 Correct
    # 5748679033029 Correct
    main()
