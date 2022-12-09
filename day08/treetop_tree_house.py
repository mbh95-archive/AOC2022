def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        return [[int(c) for c in line.strip()] for line in file.readlines()]


def part1():
    map = read_input()
    visible = [[False for _ in range(len(r))] for r in map]
    num_rows = len(map)
    num_cols = len(map[0])

    for r in range(num_rows):
        max_height = map[r][0]
        visible[r][0] = True
        for c in range(0, num_cols, 1):
            cur_height = map[r][c]
            if cur_height > max_height:
                max_height = cur_height
                visible[r][c] = True

        max_height = map[r][num_cols - 1]
        visible[r][num_cols - 1] = True
        for c in range(num_cols - 1, 0, -1):
            cur_height = map[r][c]
            if cur_height > max_height:
                max_height = cur_height
                visible[r][c] = True
    for c in range(num_cols):
        max_height = map[0][c]
        visible[0][c] = True
        for r in range(0, num_rows, 1):
            cur_height = map[r][c]
            if cur_height > max_height:
                max_height = cur_height
                visible[r][c] = True

        max_height = map[num_rows - 1][c]
        visible[num_rows - 1][c] = True
        for r in range(num_rows - 1, 0, -1):
            cur_height = map[r][c]
            if cur_height > max_height:
                max_height = cur_height
                visible[r][c] = True

    print(sum(sum(v for v in r) for r in visible))


def part2():
    map = read_input()
    num_rows = len(map)
    num_cols = len(map[0])

    def scenic_score(r0, c0):
        nonlocal map, num_rows, num_cols
        my_height = map[r0][c0]
        view_s = 0
        for r in range(r0 + 1, num_rows):
            view_s += 1
            if map[r][c0] >= my_height:
                break
        if view_s == 0:
            return 0
        view_n = 0
        for r in range(r0 - 1, -1, -1):
            view_n += 1
            if map[r][c0] >= my_height:
                break
        if view_n == 0:
            return 0
        view_e = 0
        for c in range(c0 + 1, num_cols):
            view_e += 1
            if map[r0][c] >= my_height:
                break
        if view_e == 0:
            return 0
        view_w = 0
        for c in range(c0 - 1, -1, -1):
            view_w += 1
            if map[r0][c] >= my_height:
                break
        if view_w == 0:
            return 0
        return view_s * view_n * view_e * view_w

    print(max(max(scenic_score(r, c) for c in range(num_cols)) for r in range(num_rows)))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
