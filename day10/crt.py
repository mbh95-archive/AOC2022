def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        for line in file:
            if line.startswith("noop"):
                yield 0
            elif line.startswith("addx"):
                yield 0
                yield int(line[4:].strip())


def part1():
    xreg = 1
    clock = 1
    sigsum = 0
    for dreg in read_input():
        if (clock - 20) % 40 == 0:
            print("%s - %s" % (clock, xreg))
            sigsum += xreg * clock
            if clock == 220:
                break
        xreg += dreg
        clock += 1

    print(sigsum)


def part2():
    xreg = 1
    clock = 1
    for dreg in read_input():
        px = (clock - 1) % 40
        if abs(xreg - px) <= 1:
            print("#", end="")
        else:
            print(".", end="")
        if px == 39:
            print("")
        xreg += dreg
        clock += 1
    pass


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
