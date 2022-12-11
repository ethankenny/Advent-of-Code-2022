data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip().split(' '))

x, cycle, num = 1, 0, 0
strengths = 0
crt = []

for val in data:
    match val[0]:
        case 'noop':
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                strengths += (x * cycle)

            draw = (cycle-1) % 40
            if draw == x or draw == x-1 or draw == x+1:
                crt.append('#')
            else:
                crt.append('.')

        case 'addx':
            for i in range(2):
                cycle += 1
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    strengths += (x * cycle)
                
                draw = (cycle-1) % 40
                if draw == x or draw == x-1 or draw == x+1:
                    crt.append('#')
                else:
                    crt.append('.')

            x += int(val[1])

print("Part 1: %s\nPart 2:" % strengths)
lines = [crt[0:40], crt[40:80], crt[80:120], crt[120:160], crt[160:200], crt[200:240]]
for line in lines:
    print(line)
