data = []

with open('input.txt') as file:
    for line in file:
        if 'move' in line:
            data.append(line.strip().split(' '))

crates = [list("ZJNWPS"), list("GST"), list("VQRLH"), list("VSTD"), list("QZTDBMJ"), list("MWTJDCZL"), list("LPMWGTJ"), list("NGMTBFQH"), list("RDGCPBQW")]

answer_1, answer_2 = "", ""
for val in data:
    for i in range(int(val[1])):
        crate = crates[int(val[3])-1].pop()
        crates[int(val[5])-1].append(crate)

for crate in crates:
    answer_1 += crate[-1]

crates = [list("ZJNWPS"), list("GST"), list("VQRLH"), list("VSTD"), list("QZTDBMJ"), list("MWTJDCZL"), list("LPMWGTJ"), list("NGMTBFQH"), list("RDGCPBQW")]

for val in data:
    group = []
    for i in range(int(val[1])):
        crate = crates[int(val[3])-1].pop()
        group.append(crate)

    group.reverse()
    for c in group:
        crates[int(val[5])-1].append(c)

for crate in crates:
    answer_2 += crate[-1]

print("Part 1: %s\nPart 2: %s" % (answer_1, answer_2))