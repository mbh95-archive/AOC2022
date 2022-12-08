from collections import defaultdict
from collections import deque


def scan_input(filename="input.txt"):
    with open(filename, "r") as file:
        while True:
            c = file.read(1)
            if not c:
                return None
            yield c


def end_of_first_sequence_of_n_distinct_chars(scanner, n):
    if n <= 0:
        return None
    counts = defaultdict(int)
    buffer = deque([], n)
    num_unique = 0
    for _ in range(n):
        c = next(scanner)
        buffer.append(c)
        counts[c] += 1
        if counts[c] == 1:
            num_unique += 1
    if num_unique == n:
        return n
    end_index = n
    for new in scanner:
        end_index += 1
        old = buffer.popleft()
        buffer.append(new)
        counts[new] += 1
        # If the new char wasn't in last n before, then it a new unique char
        if counts[new] == 1:
            num_unique += 1
        counts[old] -= 1
        # If the old char isn't in the last n, then we removed a unique char
        if counts[old] == 0:
            num_unique -= 1
        if num_unique == n:
            return end_index


def part1():
    print(end_of_first_sequence_of_n_distinct_chars(scan_input(), 4))


def part2():
    print(end_of_first_sequence_of_n_distinct_chars(scan_input(), 14))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
