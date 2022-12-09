data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip())

def isVisible(num, lst):
    count = 0
    for val in lst:
        if val >= num:
            count += 1

    if count > 1:
        return False

    return True

def trees(num, lst):
    count = 0
    for i in range(1, len(lst)):
        count += 1
        if lst[i] >= num:
            break

    return count

rotated = []
for column in zip(*data):
    rotated.append(column)

num_visible = len(data) * len(data[0])
num_trees = []
for i in range(len(data)):
    for j in range(len(data[i])):
        num = data[i][j]
        row_1 = list(data[i][0:j+1])
        row_2 = list(data[i][j:len(data[i])])

        col_1 = list(rotated[j][0:i+1])
        col_2 = list(rotated[j][i:len(data[i])])

        row_1.reverse()
        col_1.reverse()

        if not isVisible(num, row_1) and not isVisible(num, row_2) and not isVisible(num, col_1) and not isVisible(num, col_2):
            num_visible -= 1

        num_trees.append(trees(num, row_1) * trees(num, row_2) * trees(num, col_1) * trees(num, col_2))

print("Part 1: %s\nPart 2: %s" % (num_visible, max(num_trees)))
