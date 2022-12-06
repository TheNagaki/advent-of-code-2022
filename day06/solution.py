def read_input():
    with open('../day06/input.txt') as f:
        array = f.readlines()
    f.close()
    return array


def string_has_duplicates(string):
    for char in string:
        if string.count(char) > 1:
            return True
    return False


def get_last_position_of_first_signal(size):
    first_signals = []
    for line in read_input():
        line = line.strip()
        if line != '\n' and len(line) >= size:
            signal = line[:size]
            i = 0
            while string_has_duplicates(signal) and i + size < len(line):
                i += 1
                signal = line[i:size + i]
            first_signals.append(f'{i + size}')
    return "\n".join(first_signals)


def part1():
    return get_last_position_of_first_signal(4)


def part2():
    return get_last_position_of_first_signal(14)
