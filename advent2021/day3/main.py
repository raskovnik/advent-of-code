import os, sys

def part1():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        g_rate, e_rate = "", ""
        c = f.readlines()
        for i in range(0, len(c[0]) - 1):
            if [x[i] for x in c].count("1") > [x[i] for x in c].count("0"):
                g_rate += "1"
                e_rate += "0"
            else:
                g_rate += "0"
                e_rate += "1"

    return int(g_rate, 2) * int(e_rate, 2)

def part2():
    with open(os.path.join(sys.path[0], 'input.txt'), 'r') as f:
        c = f.readlines()
        c_compare, o_compare, csr, ogr = "", "", c ,c
        for i in range(0, 12):
            if len(ogr) == 1:
                break
                
            if [x[i] for x in ogr].count("1") > [x[i] for x in ogr].count("0"):
                o_compare += "1"
                ogr = [x for x in ogr if x[:i+1] == o_compare]

            if [x[i] for x in ogr].count("1") < [x[i] for x in ogr].count("0"):
                o_compare += "0"
                ogr = [x for x in ogr if x[:i+1] == o_compare]

            if [x[i] for x in ogr].count("1") == [x[i] for x in ogr].count("0"):
                o_compare += "1"
                ogr = [x for x in ogr if x[:i+1] == o_compare]

        for i in range(0, 12):
            if len(csr) == 1:
                break
            if [x[i] for x in csr].count("1") > [x[i] for x in csr].count("0"):
                c_compare += "0"
                csr = [x for x in csr if x[:i+1] == c_compare]
                continue
            if [x[i] for x in csr].count("1") < [x[i] for x in csr].count("0"):
                c_compare += "1"
                csr = [x for x in csr if x[:i+1] == c_compare]
                continue
            if [x[i] for x in csr].count("1") == [x[i] for x in csr].count("0"):
                c_compare += "0"
                csr = [x for x in csr if x[:i+1] == c_compare] 

        return int(csr[0], 2) * int(ogr[0], 2)


print(part2())
#960679