import re


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            yield line


def parse_stacks(input):
    stacks = None
    line = next(input)
    next_line = next(input)
    while True:
        row = line[1::4]
        if stacks is None:
            stacks = [[] for _ in range(len(row))]
        for i in range(len(row)):
            if row[i] != " ":
                stacks[i].append(row[i])
        line = next_line
        next_line = next(input)
        if next_line == "":
            for s in stacks:
                s.reverse()
            return stacks


def read_steps(input):
    step_pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
    for line in input:
        yield tuple(map(int, step_pattern.match(line).groups()))


def simulate(stacks, steps):
    for (num, start, end) in steps:
        for _ in range(num):
            stacks[end - 1].append(stacks[start - 1].pop())


def part1():
    input = read_input()
    stacks = parse_stacks(input)
    steps = read_steps(input)
    simulate(stacks, steps)
    print("".join([stack[-1] for stack in stacks]))
    # steps = parse_steps(input)


def simulate9001(stacks, steps):
    for (num, start, end) in steps:
        temp = []
        for _ in range(num):
            temp.append(stacks[start - 1].pop())
        for _ in range(num):
            stacks[end - 1].append(temp.pop())


def part2():
    input = read_input()
    stacks = parse_stacks(input)
    steps = read_steps(input)
    simulate9001(stacks, steps)
    print("".join([stack[-1] for stack in stacks]))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
