from pathlib import Path


def get_inputs():
    lst = Path("day04/test.txt").read_text().split("\n")

    return lst


def get_response_part1(input):

    for line in input:
        for ch in line:
            if ch == "X":
                pass


def get_response_part2(input):

    print(input)


if __name__ == "__main__":
    lst = get_inputs()
    print(f"Party 01: {get_response_part1(lst)}")
    # print(f"Party 02: {get_response_part2(lst)}")
