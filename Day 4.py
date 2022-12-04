data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip().split(','))

count_1, count_2 = 0, 0
for val in data:
    first_first = int(val[0].split('-')[0])
    first_second = int(val[0].split('-')[1])
    second_first = int(val[1].split('-')[0])
    second_second = int(val[1].split('-')[1])

    if (first_first <= second_first and first_second >= second_second):
        count_1 += 1
    elif (second_first <= first_first and second_second >= first_second):
        count_1 += 1

    for i in range(first_first, first_second+1):
        if (i >= second_first and i <= second_second):
            count_2 += 1
            break

    
print("Part 1: %s\nPart 2: %s" % (count_1, count_2))