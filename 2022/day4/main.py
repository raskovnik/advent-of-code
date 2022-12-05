import os
import sys

class Solution:
    def __init__(self):
        print(self.part1())
        print(self.part2())

    def part1(self):
        c = 0
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            lines = file.read().split("\n")
            for line in lines:
                w, x = line.split(",")[0].split("-")
                y, z = line.split(",")[1].split("-")
                if (int(w) <= int(y) and int(x) >= int(z)) or (int(y) <= int(w) and int(x) <= int(z)): c+= 1
        
        return c

    def part2(self):
        c = 0
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            lines = file.read().split("\n")
            for line in lines:
                w, x = line.split(",")[0].split("-")
                y, z = line.split(",")[1].split("-")
                if int(x) >= int(y) and int(w) <= int(z): c+= 1
            
        return c
if __name__ == "__main__":
    Solution()