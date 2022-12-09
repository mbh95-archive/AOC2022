def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        return [[int(c) for c in line.strip()] for line in file.readlines()]


def part1():
    map = read_input()
    visible = [[False for _ in range(len(r))] for r in map]
    num_rows = len(map)
    num_cols = len(map[0])

    def out_of_bounds(r, c):
        nonlocal num_rows, num_cols
        return r < 0 or r >= num_rows or c < 0 or c >= num_cols

    def cast_ray(path):
        nonlocal map, visible, num_rows, num_cols
        max_height = -1
        for r, c in path:
            if out_of_bounds(r, c):
                return
            cur_height = map[r][c]
            if cur_height > max_height:
                max_height = cur_height
                visible[r][c] = True

    # For each row, cast a ray from left and right
    for r in range(num_rows):
        cast_ray((r, c) for c in range(num_cols))
        cast_ray((r, c) for c in range(num_cols - 1, 0, -1))

    # For each col, cast a ray from top and bottom
    for c in range(num_cols):
        cast_ray((r, c) for r in range(num_rows))
        cast_ray((r, c) for r in range(num_rows - 1, 0, -1))

    # Count the visible trees

    print(sum(sum(v for v in r) for r in visible))


def part2():
    map = read_input()
    num_rows = len(map)
    num_cols = len(map[0])

    def count_visible_trees(path, starting_height):
        nonlocal map
        num_visible = 0
        for r, c in path:
            num_visible += 1
            if map[r][c] >= starting_height:
                break
        return num_visible

    def scenic_score(r0, c0):
        nonlocal map, num_rows, num_cols
        my_height = map[r0][c0]
        return count_visible_trees(((r, c0) for r in range(r0 + 1, num_rows)), my_height) \
            * count_visible_trees(((r, c0) for r in range(r0 - 1, -1, -1)), my_height) \
            * count_visible_trees(((r0, c) for c in range(c0 + 1, num_cols)), my_height) \
            * count_visible_trees(((r0, c) for c in range(c0 - 1, -1, -1)), my_height)

    all_trees = ((r, c) for c in range(num_cols) for r in range(num_rows))
    print(max(scenic_score(r, c) for (r, c) in all_trees))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
