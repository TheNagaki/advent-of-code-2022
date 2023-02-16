class Monkey:
    inspections_nb = 0

    def __init__(self, number, items, operation, test):
        self.monkey2 = None
        self.monkey1 = None
        self.operation = operation
        self.test_item = test
        self.number = number
        self.items = [self.operation(item) for item in items]

    def set(self, first_monkey, second_monkey):
        self.monkey1 = first_monkey
        self.monkey2 = second_monkey

    def test(self, item):
        if self.test_item(item):
            # print(f"Item {item} goes to Monkey{self.monkey1.number}")
            self.monkey1.add_item(item)
        else:
            # print(f"Item {item} goes to Monkey{self.monkey2.number}")
            self.monkey2.add_item(item)

    def add_item(self, item):
        self.items.append(self.operation(item))

    def inspect(self):
        self.inspections_nb += 1
        item = self.items[0]
        self.items = self.items[1:]
        # print(f">\tMonkey{self.number} inspects {item}")
        return item


def relief(worry_lvl):
    return int((worry_lvl - worry_lvl % 3) / 3)


def init_monkeys_input():
    monkey0 = Monkey(0, [56, 52, 58, 96, 70, 75, 72], lambda x: x * 17, lambda x: x % 11 == 0)
    monkey1 = Monkey(1, [75, 58, 86, 80, 55, 81], lambda x: x + 7, lambda x: x % 3 == 0)
    monkey2 = Monkey(2, [73, 68, 73, 90], lambda x: x * x, lambda x: x % 5 == 0)
    monkey3 = Monkey(3, [72, 89, 55, 51, 59], lambda x: x + 1, lambda x: x % 7 == 0)
    monkey4 = Monkey(4, [76, 76, 91], lambda x: x * 3, lambda x: x % 19 == 0)
    monkey5 = Monkey(5, [88], lambda x: x + 4, lambda x: x % 2 == 0)
    monkey6 = Monkey(6, [64, 63, 56, 50, 77, 55, 55, 86], lambda x: x + 8, lambda x: x % 13 == 0)
    monkey7 = Monkey(7, [79, 58], lambda x: x + 6, lambda x: x % 17 == 0)

    monkey0.set(monkey2, monkey3)
    monkey1.set(monkey6, monkey5)
    monkey2.set(monkey1, monkey7)
    monkey3.set(monkey2, monkey7)
    monkey4.set(monkey0, monkey3)
    monkey5.set(monkey6, monkey4)
    monkey6.set(monkey4, monkey0)
    monkey7.set(monkey1, monkey5)
    return [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]


def init_monkeys_test():
    monkey0 = Monkey(0, [79, 98], lambda x: x * 19, lambda x: x % 23 == 0)
    monkey1 = Monkey(1, [54, 65, 75, 74], lambda x: x + 6, lambda x: x % 19 == 0)
    monkey2 = Monkey(2, [79, 60, 97], lambda x: x * x, lambda x: x % 13 == 0)
    monkey3 = Monkey(3, [74], lambda x: x + 3, lambda x: x % 17 == 0)
    monkey0.set(monkey2, monkey3)
    monkey1.set(monkey2, monkey0)
    monkey2.set(monkey1, monkey3)
    monkey3.set(monkey0, monkey1)
    return [monkey0, monkey1, monkey2, monkey3]


def turn_part1(monkeys_list, index):
    monkey = monkeys_list[index]
    # print("-" * 20)
    for i in range(len(monkey.items)):
        item = monkey.inspect()
        item = relief(item)
        monkey.test(item)


def part1():
    monkeys_list = init_monkeys_input()
    for j in range(20):
        for i in range(len(monkeys_list)):
            turn_part1(monkeys_list, i)
        # print(f"After round {j + 1} :")
        # for monkey in monkeys_list:
        #     print(f"Monkey{monkey.number}: {', '.join([str(item) for item in monkey.items])}")
        # print("-" * 20)
    max_inspection = max([monkey.inspections_nb for monkey in monkeys_list])
    second_max_inspection = max(
        [monkey.inspections_nb for monkey in monkeys_list if monkey.inspections_nb != max_inspection])
    # for monkey in monkeys_list:
    #     print(f"Monkey{monkey.number} inspected {monkey.inspections_nb} items")
    return max_inspection * second_max_inspection


def turn_part2(monkeys_list, index):
    monkey = monkeys_list[index]
    for i in range(len(monkey.items)):
        item = monkey.inspect()
        monkey.test(item)


def part2():
    monkeys_list = init_monkeys_input()
    for j in range(10000):
        print(j)
        for i in range(len(monkeys_list)):
            monkey = monkeys_list[i]
            for _ in range(len(monkey.items)):
                item = monkey.inspect()
                monkey.test(item)
    for monkey in monkeys_list:
        print(f"Monkey{monkey.number} inspected {monkey.inspections_nb} items")
    max_inspection = max([monkey.inspections_nb for monkey in monkeys_list])
    second_max_inspection = max(
        [monkey.inspections_nb for monkey in monkeys_list if monkey.inspections_nb != max_inspection])
    return max_inspection * second_max_inspection


print(part2())
