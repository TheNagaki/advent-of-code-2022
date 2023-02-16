def read_input():
    with open("../day09/input.txt", "r") as f:
        array = [line.strip() for line in f.readlines()]
    f.close()
    return array


directions_map = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0)
}


def part1():
    array = read_input()
    unique_points = set()  # set of tuples (x, y) that are visited (unique because of set)
    head_x, head_y = 0, 0  # head is the current position of the cursor
    tail_x, tail_y = 0, 0  # tail is the position of the cursor at the previous step
    for line in array:
        direction, nb_steps = line.split(" ")
        nb_steps = int(nb_steps)
        move_x, move_y = directions_map[direction]
        unique_points.add((tail_x, tail_y))
        for i in range(nb_steps):
            head_x += move_x
            head_y += move_y
            # move tail
            delta_x = tail_x - head_x
            delta_y = tail_y - head_y
            if delta_x == 0 or delta_y == 0:  # if the tail is on the same line as the head (or column)
                if abs(delta_x) >= 2:
                    tail_x += 1 if delta_x < 0 else -1
                if abs(delta_y) >= 2:
                    tail_y += 1 if delta_y < 0 else -1
            elif (abs(delta_x), abs(delta_y)) != (1, 1):  # if the tail is not on the diagonal
                tail_x += 1 if delta_x < 0 else -1
                tail_y += 1 if delta_y < 0 else -1
            unique_points.add((tail_x, tail_y))
    return len(unique_points)


def part2():
    array = read_input()
    unique_points = set()
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for line in array:
        direction, nb_steps = line.split(" ")
        nb_steps = int(nb_steps)
        move_x, move_y = directions_map[direction]
        for i in range(nb_steps):
            rope[0][0] += move_y
            rope[0][1] += move_x
            # move all rope
            for j in range(1, 10):
                prev_knot = rope[j - 1]
                delta_y = rope[j][0] - prev_knot[0]
                delta_x = rope[j][1] - prev_knot[1]
                if delta_x == 0 or delta_y == 0:  # if the tail is on the same line as the head (or column)
                    if abs(delta_x) >= 2:
                        rope[j][1] += 1 if delta_x < 0 else -1
                    if abs(delta_y) >= 2:
                        rope[j][0] += 1 if delta_y < 0 else -1
                elif (abs(delta_x), abs(delta_y)) != (1, 1):  # if the tail is not on the diagonal
                    rope[j][1] += 1 if delta_x < 0 else -1
                    rope[j][0] += 1 if delta_y < 0 else -1
            unique_points.add((rope[-1][0], rope[-1][1]))
    return len(unique_points)


print(part2())
