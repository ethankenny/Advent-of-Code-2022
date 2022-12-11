class Monkey:
    def __init__(self, items, operation, operation_num, test, true, false):
        self.items = items
        self.operation = operation
        self.operation_num = operation_num
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0
    
    def inspect(self, part_1):
        for item in self.items:
            if self.operation == '+':
                worry = item + self.operation_num
            elif self.operation == '*':
                worry = item * self.operation_num
            else:
                worry = item * item
            
            if part_1:
                worry //= 3
            else:
                worry %= total_worry

            if worry % self.test == 0:
                monkeys[self.true].items.append(worry)
            else:
                monkeys[self.false].items.append(worry)

            self.inspected += 1
        self.items = []

monkeys = [Monkey([52, 60, 85, 69, 75, 75], '*', 17, 13, 6, 7), Monkey([96, 82, 61, 99, 82, 84, 85], '+', 8, 7, 0, 7), Monkey([95, 79], '+', 6, 19, 5, 3), Monkey([88, 50, 82, 65, 77], '*', 19, 2, 4, 1), 
           Monkey([66, 90, 59, 90, 87, 63, 53, 88], '+', 7, 5, 1, 0), Monkey([92, 75, 62], '^', 2, 3, 3, 4), Monkey([94, 86, 76, 67], '+', 1, 11, 5, 2), Monkey([57], '+', 2, 17, 6, 2)]

for i in range(10):
    for monkey in monkeys:
        monkey.inspect(True)

active = []
for monk in monkeys:
    active.append(monk.inspected)

monkeys = [Monkey([52, 60, 85, 69, 75, 75], '*', 17, 13, 6, 7), Monkey([96, 82, 61, 99, 82, 84, 85], '+', 8, 7, 0, 7), Monkey([95, 79], '+', 6, 19, 5, 3), Monkey([88, 50, 82, 65, 77], '*', 19, 2, 4, 1), 
           Monkey([66, 90, 59, 90, 87, 63, 53, 88], '+', 7, 5, 1, 0), Monkey([92, 75, 62], '^', 2, 3, 3, 4), Monkey([94, 86, 76, 67], '+', 1, 11, 5, 2), Monkey([57], '+', 2, 17, 6, 2)]

total_worry = 1
for monkey in monkeys:
    total_worry *= monkey.test

for i in range(10000):
    for monkey in monkeys:
        monkey.inspect(False)

for monk in monkeys:
    active.append(monk.inspected)

active.sort()
print("Part 1: %s\nPart 2: %s" % (active[6] * active[7], active[-1] * active[-2]))
