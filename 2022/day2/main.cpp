#include <map>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

map<char, char> rules1 {
    {'X', 'C'},
    {'Z', 'B'},
    {'Y', 'A'},
};
map<char, char> rules2 {
    {'A', 'Z'},
    {'B', 'X'},
    {'C', 'Y'},
};
map<char, char> rules3 {
    {'C', 'X'},
    {'A', 'Y'},
    {'B', 'Z'},
};
map<char, char> score {
    {'X', '1'},
    {'Y', '2'},
    {'Z', '3'},
    {'A', 'X'},
    {'B', 'Y'},
    {'C', 'Z'},
};

int part1() {
    string line;
    int s = 0;
    ifstream input("data.txt");
    while (getline(input, line)) {
        char x = line[0];
        char y = line[2];
        if (rules1[y] == x) {
            s += int(score[y] - '0') + 6;
        } else if (rules2[x] == y) {
            s += int(score[y] - '0');
        } else {
            s += int(score[y] - '0') + 3;
        }
    }
    return s;
}

int part2() {
    string line;
    int s = 0;
    ifstream input("data.txt");
    while (getline(input, line)) {
        char x = line[0];
        char y = line[2];
        if (y == 'Y') {
            s += int(score[score[x]] - '0') + 3;
        } else if (y == 'X') {
            s += int(score[rules2[x]] - '0');
        } else {
            s += int(score[rules3[x]] - '0') + 6;
        }
    }
    return s;
}

int main() {
    cout << part1() << '\n';
    cout << part2() << endl;
}
