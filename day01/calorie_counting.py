import heapq


def read_input(filename="input.txt"):
    buffer = []
    with open(filename, "r") as file:
        for line in file:
            if line == "\n":
                yield buffer
                buffer = []
            else:
                buffer.append(int(line))
        yield buffer


def sum_n_largest(n):
    return sum(heapq.nlargest(n, (sum(elf) for elf in read_input())))


def part1():
    print(sum_n_largest(1))


def part2():
    print(sum_n_largest(3))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
