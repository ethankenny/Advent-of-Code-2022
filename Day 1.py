data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip())

total = 0
top = []

for i in range(len(data)):
    if data[i] == '': continue

    if i == len(data)-1:
        total += int(data[i])
        top.append(total)
        
    elif data[i+1] == '':
        total += int(data[i])
        top.append(total)
        total = 0
        
    else:
        total += int(data[i])

top.sort()

print("Part 1: %s\n Part 2: %s" % (top[-1], top[-1] + top[-2] + top[-3]))
