def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            s1, s2 = line.split(",")
            yield tuple(map(int, s1.split("-"))), tuple(map(int, s2.split("-")))


def one_contains_the_other(a, b):
    span = (min(a[0], b[0]), max(a[1], b[1]))
    return span == a or span == b


def disjoint(a, b):
    # Assume the intervals are well formed - i.e. X[0] <= X[1] for both.
    return a[1] < b[0] or a[0] > b[1]


def part1():
    print(sum(one_contains_the_other(a, b) for a, b in read_input()))


def part2():
    print(sum(not disjoint(a, b) for a, b in read_input()))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
