#include <stdio.h>
#include <ctype.h>

int isBlank(char str[]) {
    while (*str) {
        if (!isspace(*str++)) {
            return 0;
        }
    }
    return 1;
}

int part1() {
    FILE *data = fopen("test.txt", "r");
    int m, s = 0; // m is for max, s for current sum
    char curr[12];

    while (fgets(curr, 12, data)) {
        int i;
        sscanf(curr, "%d", &i);
        if (isBlank(curr)) {
            if (i > m)
                m = s;
            s = 0;
        } else {
            s += i;
        } 
    }
    return m;

}

int getMinIndex(int array[]) {
    return array[0] < array[1] ? (array[0] < array[2] ? 0 : 2) : (array[1] < array[2] ? 1: 2);
}

int part2() {
    FILE *data = fopen("test.txt", "r");
    int carry[] = {0, 0, 0};
    int m, s = 0; // m is for minimum number index, s is for current sum
    char curr[12];

    while (fgets(curr, 12, data)) {
        int i;
        sscanf(curr, "%d", &i);
        if (isBlank(curr)) {
            if (s > carry[m]) {
                carry[m] = s;
                m = getMinIndex(carry);
            }
            s = 0;
        } else {
            s += i;
        } 
    }
    if (s > carry[m])
        carry[m] = s;

    m = 0;
    for (int i = 0; i < 3; i++) {
        m += carry[i];
    }
    return m;

}

void main() {
    printf("%d\n", part2());
}
