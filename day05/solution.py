def open_input():
    with open('../day05/input.txt') as f:
        array = f.readlines()
    f.close()
    return array


def extract_instruction(instruction):
    move_str = 'move '
    from_str = ' from '
    to_str = ' to '
    index_of_from = instruction.find(from_str)
    index_of_to = instruction.index(to_str)
    return [int(instruction[len(move_str):index_of_from]), int(instruction[index_of_from + len(from_str):index_of_to]),
            int(instruction[index_of_to + len(to_str):])]


def extract_instructions(any_array):
    instructions = []
    for line in any_array:
        if 'move' in line:
            instructions.append(extract_instruction(line))
    return instructions


def fill_crates_line(line, crates):
    i = 0
    y = 0
    while i < (len(line) + 1) / 4:
        y += 4
        crate = line[y - 4:y]
        if len(crates) < i + 1:
            crates.append([])
        if crate.strip() != '':
            crates[i].insert(0, crate[1])
        i += 1


def fill_crates(any_array):
    crates = []
    for line in any_array:
        if '1' in line:
            break
        fill_crates_line(line, crates)
    return crates


def extract_top_crates(crates):
    code = ""
    for crate in crates:
        code += crate.pop() if len(crate) > 0 else ' '
    return code


def follow_instructions1(instructions, crates):
    for instruction in instructions:
        nb_of_crates = instruction[0]
        departure = instruction[1] - 1
        destination = instruction[2] - 1
        for i in range(nb_of_crates):
            crates[destination].append(crates[departure].pop())


def follow_instructions2(instructions, crates):
    for instruction in instructions:
        nb_of_crates = instruction[0]
        departure = instruction[1] - 1
        destination = instruction[2] - 1
        crates[destination].extend(crates[departure][-nb_of_crates:])
        crates[departure] = crates[departure][:-nb_of_crates]


def part1():
    array = open_input()
    crates = fill_crates(array)
    follow_instructions1(extract_instructions(array), crates)
    return extract_top_crates(crates)


def part2():
    array = open_input()
    crates = fill_crates(array)
    follow_instructions2(extract_instructions(array), crates)
    return extract_top_crates(crates)
