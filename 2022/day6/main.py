import os
import sys
from collections import Counter

class Solution:
    def __init__(self):
        print(self.part1())
        print(self.part2())

    def part1(self):
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            lines = file.readlines()[0]
            for i in range(0, len(lines) - 5): 
                if max(Counter(lines[i:i+4]).values()) == 1: return i + 4

    def part2(self):
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            lines = file.readlines()[0]
            for i in range(0, len(lines) - 14): 
                if max(Counter(lines[i:i+14]).values()) == 1: return i + 14

if __name__ == "__main__":
    Solution()