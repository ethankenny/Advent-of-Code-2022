from collections import defaultdict

data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip().split(' '))

dirs = defaultdict(int)
current = []

for val in data:
    if val[0] == '$':
        if val[1] == 'cd':
            if val[2] == '..':
                current.pop()
            else:
                current.append(val[2])
    elif val[0] != 'dir':
        size = val[0]
        path = current.copy()
        while path:
            dirs[tuple(path)] += int(size)
            path.pop()

ans_1 = 0
needed = 30000000 - (70000000 - dirs[('/',)])
dels = []
for key in dirs:
    if dirs[key] <= 100000:
        ans_1 += dirs[key]

    if dirs[key] >= needed:
        dels.append(dirs[key])

ans_2 = min(dels)

print("Part 1: %s\nPart 2: %s" % (ans_1, ans_2))