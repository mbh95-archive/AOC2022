import re


def read_input(filename="input.txt"):
    line_pattern = re.compile(r"([UDLR]) (\d+)")
    with open(filename, "r") as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            dir, dist = line_pattern.match(line).groups()
            delta = (-1, 0) if dir == "U" \
                else (1, 0) if dir == "D" \
                else (0, -1) if dir == "L" \
                else (0, 1) if dir == "R" \
                else None
            for _ in range(int(dist)):
                yield delta


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def vec2add(v, dv):
    return v[0] + dv[0], v[1] + dv[1]


def resolution(h, t):
    dr, dc = h[0] - t[0], h[1] - t[1]
    if abs(dr) <= 1 and abs(dc) <= 1:
        return 0, 0
    return sign(dr), sign(dc)


def part1():
    h = (0, 0)
    t = (0, 0)
    tail_locations = {t}

    for delta in read_input():
        h = vec2add(h, delta)
        t = vec2add(t, resolution(h, t))
        tail_locations.add(t)
    print(len(tail_locations))


def part2():
    rope = [(0, 0) for _ in range(10)]
    tail_locations = {rope[-1]}
    for delta in read_input():
        rope[0] = vec2add(rope[0], delta)
        for i in range(1, len(rope)):
            rope[i] = vec2add(rope[i], resolution(rope[i - 1], rope[i]))
        tail_locations.add(rope[-1])
    print(len(tail_locations))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
