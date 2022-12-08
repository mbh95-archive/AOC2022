def read_compartments(filename="input.txt"):
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            halfway = len(line) // 2
            yield line[:halfway], line[halfway:]


def read_groups(filename="input.txt", group_size=3):
    buffer = []
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            buffer.append(line)
            if len(buffer) == group_size:
                yield buffer
                buffer = []
    if len(buffer) != 0:
        raise Exception("Number of rucksacks is not divisible by group_size!")


def find_first_overlap(items, set):
    for item in items:
        if item in set:
            return item


def get_priority(c):
    my_ord = ord(c)
    if ord("a") <= my_ord <= ord("z"):
        return 1 + my_ord - ord("a")
    elif ord("A") <= my_ord <= ord("Z"):
        return 27 + my_ord - ord("A")


def part1():
    print(sum(get_priority(find_first_overlap(c1, set(c2))) for c1, c2 in read_compartments()))


def part2():
    print(sum(get_priority(find_first_overlap(s3, set(s1) & set(s2)))
              for (s1, s2, s3) in read_groups(group_size=3)))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
