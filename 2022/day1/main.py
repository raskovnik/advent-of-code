import os 
import sys

class Solution:
    def __init__(self):
        print(self.part1())
        print(self.part2())

    def part1(self):
        with open(os.path.join(sys.path[0], 'data.txt'), "r") as fp:
            m, s = 0, 0
            data = fp.read().split("\n")
            for item in data:
                if item == "":
                    if s > m:
                        m = s
                    s = 0
                else: s += int(item)
            return m

    def part2(self):
        with open(os.path.join(sys.path[0], 'data.txt'), "r") as fp:
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
    Solution()