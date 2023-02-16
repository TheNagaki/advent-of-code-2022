DEFAULT_SYMBOL = "."
REPLACED_SYMBOL = "#"


def add_y_before(array):
    array.insert(0, [DEFAULT_SYMBOL] * len(array[0]))


def add_y_after(array):
    array.append([DEFAULT_SYMBOL] * len(array[0]))


def add_column_after(array):
    for row in array:
        row.append(DEFAULT_SYMBOL)


def add_column_before(array):
    for row in array:
        row.insert(0, DEFAULT_SYMBOL)


def read_input():
    with open("../day09/input.txt") as f:
        array = f.readlines()
    f.close()
    for i in range(len(array)):
        array[i] = array[i].strip()
    return array


def extract_instruction(line):
    return line.split(" ")


def move_tail(array, pos_head, pos_tail):
    array[pos_tail[0]][pos_tail[1]] = REPLACED_SYMBOL
    if abs(pos_head[0] - pos_tail[0]) <= 1 and abs(pos_head[1] - pos_tail[1]) <= 1:
        # print("tail is close to head")
        # covers the case where the head is on the same line or column as the tail or on the diagonal
        pass
    elif pos_head[0] == pos_tail[0]:  # same y but different x
        # print("same y but different x")
        pos_tail[1] += 1 if pos_head[1] > pos_tail[1] else -1  # move the tail on the same line as the head
    elif pos_head[1] == pos_tail[1]:  # same x but different y
        # print("same x but different y")
        pos_tail[0] += 1 if pos_head[0] > pos_tail[0] else -1  # move the tail on the same line as the head
    else:  # different x and y
        # print("different x and y")
        pos_tail[0] += 1 if pos_head[0] > pos_tail[0] else -1  # move the tail on the same line as the head
        pos_tail[1] += 1 if pos_head[1] > pos_tail[1] else -1  # move the tail on the same column as the head
    # array[pos_head[0]][pos_head[1]] = "C"
    # print_array(array)


def move_right(array, nb_steps, position_head, position_tail):
    if len(array[position_head[0]]) - 1 < position_head[1] + nb_steps:
        for i in range(position_head[1] + nb_steps - len(array[position_head[0]]) + 1):
            add_column_after(array)
    for i in range(nb_steps):
        # array[position_head[0]][position_head[1]] = "H"
        position_head[1] += 1
        move_tail(array, position_head, position_tail)


def move_left(array, nb_steps, position_head, position_tail):
    if position_head[1] - nb_steps < 0:
        for i in range(-1 * (position_head[1] - nb_steps)):
            add_column_before(array)
            position_head[1] += 1
            position_tail[1] += 1
    for i in range(nb_steps):
        # array[position_head[0]][position_head[1]] = "H"
        position_head[1] -= 1
        move_tail(array, position_head, position_tail)


def move_up(array, nb_steps, position_head, position_tail):
    if position_head[0] + nb_steps > len(array) - 1:
        for i in range(position_head[0] + nb_steps - len(array) + 1):
            add_y_after(array)
    for i in range(nb_steps):
        # array[position_head[0]][position_head[1]] = "H"
        position_head[0] += 1
        move_tail(array, position_head, position_tail)


def move_down(array, nb_steps, position_head, position_tail):
    if position_head[0] - nb_steps < 0:
        for i in range(-1 * (position_head[0] - nb_steps)):
            add_y_before(array)
            position_head[0] += 1
            position_tail[0] += 1
    for i in range(nb_steps):
        # array[position_head[0]][position_head[1]] = "H"
        position_head[0] -= 1
        move_tail(array, position_head, position_tail)


def part1():
    instructions = read_input()
    array = [["H"]]
    current_head_position = [0, 0]
    current_tail_position = [0, 0]
    for i in range(len(instructions)):
        current_instruction = instructions[i].split(" ")
        # print(f"{current_instruction[0]} {current_instruction[1]}")
        if current_instruction[0] == "R":
            move_right(array, int(current_instruction[1]), current_head_position, current_tail_position)
        elif current_instruction[0] == "L":
            move_left(array, int(current_instruction[1]), current_head_position, current_tail_position)
        elif current_instruction[0] == "U":
            move_up(array, int(current_instruction[1]), current_head_position, current_tail_position)
        elif current_instruction[0] == "D":
            move_down(array, int(current_instruction[1]), current_head_position, current_tail_position)
    count = 0
    for row in array:
        for column in row:
            if column == REPLACED_SYMBOL:
                count += 1
    # print_array(array)
    print("array size: " + str(len(array)) + "*" + str(len(array[0])))
    return "does not work yet"


def print_array(array):
    for row in array:
        row_str = ""
        for column in row:
            row_str += "0" if column == DEFAULT_SYMBOL else "1"
        print(row_str)
    print("----------------")


def part2():
    return "does not work yet"