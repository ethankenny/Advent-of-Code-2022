data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip().split())

total1, total2 = 0, 0

for val in data:
    if val[0] == 'A':
        if val[1] == 'X':
            total1 += 4
        elif val[1] == 'Y':
            total1 += 8
        else:
            total1 += 3
    elif val[0] == 'B':
        if val[1] == 'X':
            total1 += 1
        elif val[1] == 'Y':
            total1 += 5
        else:
            total1 += 9
    else:
        if val[1] == 'X':
            total1 += 7
        elif val[1] == 'Y':
            total1 += 2
        else:
            total1 += 6

for val in data:
    if val[0] == 'A':
        if val[1] == 'X':
            total2 += 3
        elif val[1] == 'Y':
            total2 += 4
        else:
            total2 += 8
    elif val[0] == 'B':
        if val[1] == 'X':
            total2 += 1
        elif val[1] == 'Y':
            total2 += 5
        else:
            total2 += 9
    else:
        if val[1] == 'X':
            total2 += 2
        elif val[1] == 'Y':
            total2 += 6
        else:
            total2 += 7


print("Part 1: %s\nPart 2: %s" % (total1, total2))
