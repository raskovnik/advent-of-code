import os, sys

def part1():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        days = [int(c) for c in [x for x in f][0].split(",")]
        for _ in range(18):
            temp = []
            for x in days:
                if x == 0:
                    temp.append(8)
                    temp.append(6)

                else:
                    temp.append(x - 1)

            days = temp
    return len(days)
print(part1())

def part2():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        days = [int(c) for c in [x for x in f][0].split(",")]
        fish = {}
        for i in range(9):
            fish[i] = days.count(i)
        for _ in range(256):
            new_fish = fish[0]
            for c in range(0, 8):
                fish[c] = fish[c + 1]
            fish[8] = new_fish
            fish[6] += new_fish

    return sum(fish.values())

print(part2())
