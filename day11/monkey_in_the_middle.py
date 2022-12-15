import re
import math
from collections import deque

class Monkey:
    def __init__(self, name, starting_items, operation, test_mod, true_monkey, false_monkey):
        self.name = name
        self.items = starting_items
        self.operation = operation
        self.test_mod = test_mod
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspection_count = 0

    def catch(self, worry):
        self.items.append(worry)

    def take_turn(self, divide_by_three=True, lcm=None):
        print("Start turn: %s" % self.name)
        while self.items:
            self.inspection_count += 1
            worry = self.items.popleft()
            print("\tInspect %d" % worry)
            worry = self.operation(worry)
            if lcm:
                worry = worry % lcm
            print("\t\tWorry -> %d" % worry)
            if divide_by_three:
                worry = worry // 3
                print("\t\tWorry / 3 -> %d" % worry)
            if worry % self.test_mod == 0:
                print("\t\tTrue; %d is divisible by %d; toss to %d" % (worry, self.test_mod, self.true_monkey))
                yield self.true_monkey, worry
            else:
                print("\t\tFalse; %d not divisible by %d; toss to %d" % (worry, self.test_mod, self.false_monkey))
                yield self.false_monkey, worry


def read_input(filename="input.txt"):
    def create_op(op_rhs):
        operator = op_rhs[4]
        operand = op_rhs[6:]
        if operand == "old":
            if operator == "*":
                return lambda x: x * x
            elif operator == "+":
                return lambda x: x + x
        else:
            if operator == "*":
                return lambda x: x * int(operand)
            elif operator == "+":
                return lambda x: x + int(operand)

    op_pattern = re.compile("\s*Operation: new = (.*)")
    test_pattern = re.compile("\s*Test: divisible by (\d+)")
    true_pattern = re.compile(("\s*If true: throw to monkey (\d+)"))
    false_pattern = re.compile(("\s*If false: throw to monkey (\d+)"))
    with open(filename, "r") as file:
        while True:
            name = file.readline()[:-2]
            starting_items = deque(int(x) for x in re.findall(r"\d+", file.readline()))
            operation = create_op(op_pattern.match(file.readline()).groups()[0])
            test_mod = int(test_pattern.match(file.readline()).groups()[0])
            true_monkey = int(true_pattern.match(file.readline()).groups()[0])
            false_monkey = int(false_pattern.match(file.readline()).groups()[0])
            yield Monkey(name, starting_items, operation, test_mod, true_monkey, false_monkey)
            if not file.readline():
                return


def part1():
    monkeys = [m for m in read_input()]
    for round in range(20):
        for monkey in monkeys:
            for dest, worry in monkey.take_turn():
                monkeys[dest].catch(worry)
    monkey_business = math.prod(sorted((m.inspection_count for m in monkeys), reverse=True)[:2])
    print(monkey_business)


def part2():
    monkeys = [m for m in read_input()]
    lcm = math.lcm(*(m.test_mod for m in monkeys))
    for round in range(10000):
        for monkey in monkeys:
            for dest, worry in monkey.take_turn(divide_by_three=False, lcm=lcm):
                monkeys[dest].catch(worry)
    monkey_business = math.prod(sorted((m.inspection_count for m in monkeys), reverse=True)[:2])
    print(monkey_business)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
