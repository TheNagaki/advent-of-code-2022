def fully_contains(elf1, elf2):
    ranges1 = extract_elf_ranges(elf1)
    ranges2 = extract_elf_ranges(elf2)
    return (ranges1[0] <= ranges2[0] and ranges1[1] >= ranges2[1]) or (
            ranges1[0] >= ranges2[0] and ranges1[1] <= ranges2[1])


def overlaps(elf1, elf2):
    ranges1 = extract_elf_ranges(elf1)
    ranges2 = extract_elf_ranges(elf2)
    return ranges1[0] <= ranges2[0] <= ranges1[1] or ranges1[0] <= ranges2[1] <= ranges1[1] or ranges2[0] <= ranges1[
        0] <= ranges2[1] or ranges2[0] <= ranges1[1] <= ranges2[1]


def extract_elf_ranges(elf):
    min_, max_ = elf.split('-')
    min_, max_ = int(min_), int(max_)  # VERY IMPORTANT: creates error in comparison otherwise
    return [min_, max_]


def part1():
    count = 0
    with open('../day04/input.txt') as f:
        for line in f:
            first_elf, second_elf = line.strip().split(',')
            if fully_contains(first_elf, second_elf):
                count += 1
    return count


def part2():
    count = 0
    with open('../day04/input.txt') as f:
        for line in f:
            first_elf, second_elf = line.strip().split(',')
            if overlaps(first_elf, second_elf):
                count += 1
    return count
