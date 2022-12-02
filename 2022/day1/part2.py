def part2():
    with open("/home/raskovnic/learning/advent-of-code/2022/day1/data.txt", "r") as fp:
        carry = [0]*3
        s = 0
        data = fp.read().split("\n")
        for item in data:
            if item == "":
                if s > min(carry):
                    carry[carry.index(min(carry))] = s
                s = 0
            else: s += int(item)
        if s > min(carry):
            carry[carry.index(min(carry))] = s

        return sum(carry)

if __name__ == "__main__":
    print(part2())