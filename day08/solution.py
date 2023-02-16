def determine_tree_is_visible(x, y, tree_map):
    if x == len(tree_map[y]) - 1 or y == len(tree_map) - 1 or x == 0 or y == 0:
        return True
    tree_size = tree_map[y][x]
    if not any(tree_map[y][i] >= tree_size for i in range(x + 1, len(tree_map[y]))):  # look east
        return True
    if not any(tree_map[y][i] >= tree_size for i in range(x - 1, -1, -1)):  # look west
        return True
    if not any(tree_map[i][x] >= tree_size for i in range(y + 1, len(tree_map))):  # look south
        return True
    if not any(tree_map[i][x] >= tree_size for i in range(y - 1, -1, -1)):  # look north
        return True
    return False


def acquire_input():
    array = []
    with open('../day08/input.txt') as f:
        for line in f:
            array.append([*line.strip()])
    f.close()
    return array


def determine_scenic_score(x, y, tree_map):
    n, s, e, w = 0, 0, 0, 0
    tree_size = tree_map[y][x]
    for i in range(x + 1, len(tree_map[y])):  # look east
        e += 1
        if tree_map[y][i] >= tree_size:
            break
    for i in range(x - 1, -1, -1):  # look west
        w += 1
        if tree_map[y][i] >= tree_size:
            break
    for i in range(y + 1, len(tree_map)):  # look south
        s += 1
        if tree_map[i][x] >= tree_size:
            break
    for i in range(y - 1, -1, -1):  # look north
        n += 1
        if tree_map[i][x] >= tree_size:
            break
    # print(f"---{n}---")
    # print(f"{w}-----{e}")
    # print(f"---{s}---")
    return n * s * e * w


def part1():
    count = 0
    array = acquire_input()
    for i in range(len(array)):
        for j in range(len(array[i])):
            if determine_tree_is_visible(j, i, array):
                count += 1
    return count


def part2():
    max_score = 0
    array = acquire_input()
    for i in range(len(array)):
        for j in range(len(array[i])):
            score = determine_scenic_score(j, i, array)
            if score > max_score:
                max_score = score
    return max_score
