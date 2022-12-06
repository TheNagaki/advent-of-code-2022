def read_input():
    with open('../day06/test.txt') as f:
        return f.readlines()


def string_has_duplicates(string):
    for char in string:
        if string.count(char) > 1:
            return True
    return False


def get_position_of_first_signal(size):
    first_signals = []
    input_file = read_input()
    for line in input_file:
        line = line.strip()
        if line != '\n' and len(line) > 3:
            signal = line[:size]
            i = 0
            while string_has_duplicates(signal):
                i += 1
                signal = line[i:size + i]
            first_signals.append(f'{i + size}')
    return "\n".join(first_signals)


def part1():
    return get_position_of_first_signal(4)


def part2():
    return get_position_of_first_signal(14)


print(part1())

print(part2())
