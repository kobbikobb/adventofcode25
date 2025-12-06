from _utils.text_utils import read_input_data
from day04.part1 import get_result_part_1
from day04.part2 import get_result_part_2

def main():
    """The solution"""
    data = read_input_data("input.txt")
    result1 = get_result_part_1(data)
    result2 = get_result_part_2(data)

    print(f"result 1 :{result1}")
    print(f"result 2: {result2}")

if __name__ == "__main__":
    # 1604 Correct
    # 9397 Correct
    main()
