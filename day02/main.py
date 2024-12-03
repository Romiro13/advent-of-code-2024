from pathlib import Path


def get_inputs():

    lines = Path("day02/input.txt").open().readlines()

    lists = [r.replace("\n", "").split(" ") for r in lines]

    lists = [list(map(lambda x: int(x), arr)) for arr in lists]

    return lists


def all_bigger_or_smaller(lst):
    bigger = []
    smaller = []
    end = len(lst) - 1
    for i, v in enumerate(lst):
        if i == end:
            break
        v2 = lst[i + 1]
        bigger.append(int(v > v2))
        smaller.append(int(v < v2))

    return sum(bigger) == end or sum(smaller) == end


def is_adjacent_limit(lst):
    limit = []
    end = len(lst) - 1
    for i, v in enumerate(lst):
        if i == end:
            break
        v2 = lst[i + 1]
        limit.append(int(abs(v - v2) <= 3))

    return sum(limit) == end


def safe_by_remove_a_single(lst: list[int]):
    limit = []
    for i, _ in enumerate(lst):
        arr = lst.copy()
        arr.pop(i)
        limit.append(is_adjacent_limit(arr) and all_bigger_or_smaller(arr))

    return sum(limit) > 0


def get_response_part1(lst: list[list[int]]):

    results = []
    for row in lst:
        results.append(is_adjacent_limit(row) and all_bigger_or_smaller(row))

    return sum(results)


def get_response_part2(lst: list[list[int]]):

    results = []
    for row in lst:
        results.append(is_adjacent_limit(row) and all_bigger_or_smaller(row))
        if not results[-1]:
            results[-1] = safe_by_remove_a_single(row)

    return sum(results)


if __name__ == "__main__":
    lst = get_inputs()
    print(f"Party 01: {get_response_part1(lst)}")
    print(f"Party 02: {get_response_part2(lst)}")
