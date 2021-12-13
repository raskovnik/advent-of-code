import os, sys

with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
    lines = f.readlines()
    count = 3
    for i in range(len(lines)):
        if lines[i] > lines[i - 3]:
            count += 1
        
print(count)