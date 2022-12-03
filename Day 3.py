data_1, data_2 = [], []

with open('input.txt') as file:
    for line in file:
        str = line.strip()
        data_1.append([str[0:int(len(str)/2)], str[int(len(str)/2):int(len(str))]])
        data_2.append(str)

total_1, total_2 = 0, 0
unique_1, unique_2 = [], []

for val in data_1:
    chars = set()

    for c in val[0]:
        chars.add(c)
    for ch in val[1]:
        if ch in chars:
            unique_1.append(ch)
            break

for i in range (0, len(data_2), 3):
    three = [data_2[i], data_2[i+1], data_2[i+2]]
    chars = set()
    both = set()
    
    for c in three[0]:
        chars.add(c)

    for ch in three[1]:
        if ch in chars:
            both.add(ch)

    for cha in three[2]:
        if cha in both:
            unique_2.append(cha)
            break


for un in unique_1:
    if un in 'abcdefghijklmnopqrstuvwxyz':
        total_1 += ord(un)-96
    else:
        total_1 += ord(un)-38

for un in unique_2:
    if un in 'abcdefghijklmnopqrstuvwxyz':
        total_2 += ord(un)-96
    else:
        total_2 += ord(un)-38
        

print("Part 1: %s\nPart 2: %s" % (total_1, total_2))