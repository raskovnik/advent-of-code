import os, sys

def part1():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    commands = f.readlines()
    u, d, f = 0, 0, 0
    for i in range(len(commands)):
        if commands[i].split(" ")[0] == "forward":
            f += int(commands[i].split(" ")[1])
        if commands[i].split(" ")[0] == "up":
            u += int(commands[i].split(" ")[1])
        if commands[i].split(" ")[0] == "down":
            d += int(commands[i].split(" ")[1])
        
    return (d - u) * f

def part2():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    commands = f.readlines()
    hp, aim, depth = 0, 0, 0
    for i in range(len(commands)):
        if commands[i].split(" ")[0] == "forward":
            hp += int(commands[i].split(" ")[1])
            depth += aim * int(commands[i].split(" ")[1])
        if commands[i].split(" ")[0] == "up":
            aim -= int(commands[i].split(" ")[1])
        if commands[i].split(" ")[0] == "down":
            aim += int(commands[i].split(" ")[1])
        
    return (hp * depth)