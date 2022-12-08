from collections import defaultdict


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            yield line


def solution():
    path = ["/"]
    lsd = defaultdict(bool)
    sizes = defaultdict(int)

    scanner = read_input()
    line = next(scanner)
    next_line = None
    prev_line = None

    def cd(arg):
        nonlocal path
        # print("CD %s" % arg)
        if arg == "/":
            path = ["/"]
        elif arg == "..":
            path.pop()
        else:
            # I guess we don't need to validate that we are cd'ing to path we've seen via ls already?
            path.append(arg)

    def pwd():
        nonlocal path
        return "/".join(path)

    def ls():
        nonlocal lsd, sizes, line
        # print("LS %s" % path)
        advance_scanner()
        while line:
            if line.startswith("$"):
                # back up so that the next command isn't skipped.
                rewind_scanner()
                return
            elif line.startswith("dir"):
                # print(line)
                pass
            elif not lsd[pwd()]:
                # If we call ls on the same directory twice we don't want to double count file sizes.
                sz = int(line.split(" ")[0])
                tmp = []
                while len(path):
                    sizes[pwd()] += sz
                    tmp.append(path.pop())
                tmp.reverse()
                path.extend(tmp)

            advance_scanner()
        lsd[pwd()] = True

    def advance_scanner():
        nonlocal scanner, line, prev_line, next_line
        prev_line = line
        if next_line:
            line = next_line
            next_line = None
        else:
            try:
                line = next(scanner)
            except StopIteration:
                line = None

    def rewind_scanner():
        nonlocal line, prev_line, next_line
        if next_line:
            raise Exception("Two calls to prev_line() in a row. Only one line is buffered.")
        next_line = line
        line = prev_line

    while line:
        if line.startswith("$ cd"):
            cd(line[5:])
        elif line.startswith("$ ls"):
            ls()
        advance_scanner()

    print(sizes)
    print(sum(size for (dir, size) in sizes.items() if size <= 100000))

    free_space = 70000000 - sizes["/"]
    print(min(size for (dir, size) in sizes.items() if free_space + size >= 30000000))


def main():
    solution()


if __name__ == "__main__":
    main()
