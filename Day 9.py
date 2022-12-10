# may god have mercy on my soul
data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip())

path = [[0, 0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

visited_1 = set()
visited_2 = set()

for val in data:
    dir, amnt = val.split(' ')
    
    for _ in range(int(amnt)):
        match dir:
            case "U":
                path[0][1] += 1
            case "D":
                path[0][1] -= 1
            case "R":
                path[0][0] += 1
            case "L":
                path[0][0] -= 1
        
        for i in range(9):
            h, t = path[i], path[i+1]
            if h[0] == t[0] and h[1] == t[1]:
                pass
            elif h[0] == t[0] and h[1] - t[1] >= 2:
                t[1] = h[1] - 1
            elif h[0] == t[0] and t[1] - h[1] >= 2:
                t[1] = h[1] + 1
            elif h[0] - t[0] >= 2 and h[1] == t[1]:
                t[0] = h[0] - 1
            elif t[0] - h[0] >= 2 and h[1] == t[1]:
                t[0] = h[0] + 1
            elif abs(h[0] - t[0]) == 1 and abs(h[1] - t[1]) == 1:
                pass
            elif (h[0] == t[0] and abs(h[1] - t[1]) == 1) or (abs(h[0] - t[0]) == 1 and h[1] == t[1]):
                pass

            else:
                if t[0] < h[0] and t[1] < h[1]:
                    t[0] += 1
                    t[1] += 1
                elif t[0] < h[0] and t[1] > h[1]:
                    t[0] += 1
                    t[1] -= 1
                elif t[0] > h[0] and t[1] < h[1]:
                    t[0] -= 1
                    t[1] += 1
                else:
                    t[0] -= 1
                    t[1] -= 1
        
        visited_1.add((path[1][0], path[1][1]))
        visited_2.add((path[9][0], path[9][1]))

print("Part 1: %s\nPart 2: %s" % (len(visited_1), len(visited_2)))