import os, sys

with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
    lines = f.readlines()
    increasing = 1
    for i in range(1, len(lines)):
        if lines[i] >= lines[i - 1]:
            increasing += 1
print(increasing)
