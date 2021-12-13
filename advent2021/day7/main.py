import os, sys
from math import ceil

def part1():
    with open(os.path.join(sys.path[0], "input.txt"), 'r') as f:
        cood = [int(c) for c in [x for x in f][0].split(",")]
        cood.sort()
        fuels = 0
        median = cood[len(cood) // 2 ]

        for c in cood:
             fuels += abs(c - median)

    return fuels

def part2():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        cood = [int(c) for c in [x for x in f][0].split(",")]
        mean = ceil(sum(cood) / len(cood))
        z = []
        for i in range(mean + 1):
            a = 0
            for c in cood:
                n = abs(c - i)
                a += (n * (n + 1) // 2)
            z.append(a)

    return min(z)
    
print(part1())
print(part2())