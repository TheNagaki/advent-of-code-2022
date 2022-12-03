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


calories_per_elf = []
with open("input.txt", "r") as f:
    buffer = 0
    for line in f:
        if line != "\n":
            buffer += int(line)
        else:
            calories_per_elf.append(buffer)
            buffer = 0
f.close()

ordered_calories = sort(calories_per_elf)

maxVal1 = ordered_calories[0]
maxVal2 = ordered_calories[1]
maxVal3 = ordered_calories[2]

print(maxVal1 + maxVal2 + maxVal3)
