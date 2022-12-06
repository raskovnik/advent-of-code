import os
import sys

class Solution:
    def __init__(self):
        print(self.part1())
        print(self.part2())

    def part1(self) -> str:
        data = [[], [], [], [], [], [], [], [], []]
        with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
            lines = file.readlines()
            for line in lines:
                for i in range(1, len(line), 4):
                    if line[i] != " ":
                        stack = i % 3 if i < 9 else i % 3 + 3 if i < 25 and i != 21 else 6 if i == 21 else 9 if i == 33 else i % 3 + 6
                        data[stack-1].insert(0, (line[i]))
        file.close()
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                m, f, t = line.split(" ")[1],line.split(" ")[3],line.split(" ")[5]
                for i in range(0, int(m)):
                    data[int(t)-1].append(data[int(f)-1].pop())
        file.close()
        result = ""
        for i in range(0, 9):
            result += data[i][len(data[i])-1]

        return result

    def part2(self):
        data = [[], [], [], [], [], [], [], [], []]
        with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
            lines = file.readlines()
            for line in lines:
                for i in range(1, len(line), 4):
                    if line[i] != " ":
                        stack = i % 3 if i < 9 else i % 3 + 3 if i < 25 and i != 21 else 6 if i == 21 else 9 if i == 33 else i % 3 + 6
                        data[stack-1].insert(0, (line[i]))
        file.close()
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                m, f, t = line.split(" ")[1],line.split(" ")[3],line.split(" ")[5]
                c = []
                for i in range(0, int(m)):
                    c.insert(0, data[int(f)-1].pop())
                for x in c: data[int(t) - 1].append(x)
                c = []
        file.close()

        result = ""
        for i in range(0, 9):
            result += data[i][len(data[i])-1]

        return result

if __name__ == "__main__":
    Solution()