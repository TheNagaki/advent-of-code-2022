def read_input():
    with open('../day10/input.txt') as f:
        array = [line.strip() for line in f]
    f.close()
    return array


def part1():
    cool_cycles = [20, 60, 100, 140, 180, 220]
    sum_cool_cycles = 0
    array = read_input()
    cycle_num = 0
    x = 1
    for line in array:
        cycle_num += 1
        if cycle_num in cool_cycles:
            # print(f'Cycle {cycle_num}: {x * cycle_num}')
            sum_cool_cycles += x * cycle_num
        if "addx" in line:
            cycle_num += 1
            if cycle_num in cool_cycles:
                # print(f'Cycle {cycle_num}: {x * cycle_num}')
                sum_cool_cycles += x * cycle_num
            x += int(line.split(" ")[1])
    return sum_cool_cycles


def part2():
    x = 1
    cycle_num = 0
    row_str = ""
    array = read_input()
    for line in array:
        cycle_num += 1
        row_str += "#" if x <= cycle_num % 40 <= x + 2 else "."
        if "addx" in line:
            cycle_num += 1
            row_str += "#" if x <= cycle_num % 40 <= x + 2 else "."
            x += int(line.split(" ")[1])
    return "\n".join([row_str[i:i + 40] for i in range(0, len(row_str), 40)])
