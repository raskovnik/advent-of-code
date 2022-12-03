import os
import sys
from enum import Enum

class Score(Enum) :
    X = 1
    Y = 2
    Z = 3
    A = "X"
    B = "Y"
    C = "Z"

class Solution():
    def __init__(self):
        self.rules1 = {
            "X" : "C",
            "Z" : "B",
            "Y" : "A"
        }
        self.rules2 = {
            "A" : "Z",
            "B" : "X",
            "C" : "Y"
        }

        print(self.part1())
        print(self.part2())

    def part1(self) -> int:
        with open(os.path.join(sys.path[0], "data.txt"), "r") as file:
            m = 0
            lines = file.read().splitlines()
            for line in lines:
                p = line.split(" ")
                m += self.get_score(p[1], p[0])

        return m

    def part2(self):
        with open(os.path.join(sys.path[0], "test.txt"), "r") as file:
            m = 0
            lines = file.read().splitlines()
            for line in lines:
                p = line.split(" ")
                m += self.get_score(self.get_choice(p[0], p[1]), p[0])

        return m
        
    def get_score(self, player1, player2) -> int:
        if player1 == Score[player2].value: return Score[player1].value + 3
        if self.rules1[player1] == player2: return Score[player1].value + 6
        else: return Score[player1].value

    def get_choice(self, player1, game) -> str:
        if game == "Y": return Score[player1].value
        elif game == "X" : return self.rules2[player1]
        else: return list(self.rules1.keys())[list(self.rules1.values()).index(player1)]

if __name__=="__main__":
    Solution()