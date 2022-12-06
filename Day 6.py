data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip())

word = data[0]

for i in range(0, len(word)-3):
    lst = list(word[i:i+4])

    if len(lst) == len(set(lst)):
        ans_1 = i+4
        break

for i in range(0, len(word)-13):
    lst = list(word[i:i+14])
    
    if len(lst) == len(set(lst)):
        ans_2 = i+14
        break

print("Part 1: %s\nPart 2: %s" % (ans_1, ans_2))
    