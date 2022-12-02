def part1():
    with open("/home/raskovnic/learning/advent-of-code/2022/day1/tests.txt", "r") as fp:
        m, s = 0, 0
        data = fp.read().split("\n")
        for item in data:
            if item == "":
                if s > m:
                    m = s
                s = 0
            else: s += int(item)
        return m


if __name__ == "__main__":
    print(part1())