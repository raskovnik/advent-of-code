import os
import sys
from math import floor

class Solution():
    def __init__(self):
        print(self.part1())
        print(self.part2())

    def find_common(self, string1, string2, string3):
        c = ""
        if string3:
            for i in string1:
                for j in string2:
                    for k in string3:
                        if i == j and j == k: 
                            c = i
                            break
        else:
            for i in string1:
                for j in string2:
                    if i == j: 
                        c = i
                        break
        return c

    def part1(self):
        c = []
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            lines = file.readlines()
            for line in lines:
                c.append(self.find_common(line[0:floor(len(line) / 2)], line[floor(len(line) / 2)::], None))
        s = 0
        for k in c:
            if ord(k) <= 90: s += ord(k) - ord("A") + 27
            else: s += ord(k) - ord("a") + 1
        return s

    def part2(self):
        c, temp = [], []
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            lines = file.readlines()
            for line in lines:
                temp.append(line.strip())
                if len(temp) == 3:
                    c.append(self.find_common(temp[0], temp[1], temp[2]))
                    temp = []
        s = 0
        for k in c:
            if ord(k) <= 90: s += ord(k) - ord("A") + 27
            else: s += ord(k) - ord("a") + 1
        return s

if __name__ == "__main__":
    Solution()