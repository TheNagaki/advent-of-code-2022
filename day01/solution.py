def return_and_remove_max(array):
    max_val = 0
    for i in range(0, len(array)):
        if array[i] > max_val:
            max_val = array[i]
    array.remove(max_val)
    return max_val


def sort(array):
    sorted_array = []
    for i in range(0, len(array)):
        sorted_array.append(return_and_remove_max(array))
    return sorted_array


def read_input():
    calories_per_elf = []
    with open("../day01/input.txt", "r") as f:
        buffer = 0
        for line in f:
            if line != "\n":
                buffer += int(line)
            else:
                calories_per_elf.append(buffer)
                buffer = 0
    return sort(calories_per_elf)


def part1():
    arr = read_input()
    return arr[0]


def part2():
    arr = read_input()
    return arr[0] + arr[1] + arr[2]
