from pathlib import Path


def get_inputs():

    lines = Path("day01/input.txt").open().readlines()

    lists = [r.replace("\n", "").split("   ") for r in lines]

    la: list[int] = []
    lb: list[int] = []
    for a, b in lists:
        la.append(int(a))
        lb.append(int(b))

    return la, lb


def get_response_part1(la: list, lb: list):
    distance = []
    while len(la) > 0 and len(lb) > 0:
        a = min(la)
        b = min(lb)
        distance.append(abs(b - a))
        la.remove(a)
        lb.remove(b)

    return sum(distance)


def get_response_part2(la: list, lb: list):
    similarity = []
    for a in la:
        s = a * lb.count(a)
        similarity.append(s)

    return sum(similarity)


if __name__ == "__main__":
    la, lb = get_inputs()
    print(f"Party 01: {get_response_part1(la.copy(), lb.copy())}")
    print(f"Party 02: {get_response_part2(la, lb)}")
