def get_letter_priority(letter):
    if ord(letter) < 91:  # Majuscule
        return ord(letter) - 64 + 26  # +26 pour différencier des minuscules
    return ord(letter) - 96  # Minuscule


count = 0
with open("../day03/input.txt", "r") as file:
    for line in file:
        line = line.strip()
        length: int = len(line) // 2
        for i in range(0, length):
            if line[length:].__contains__(line[i]):
                count += get_letter_priority(line[i])
                break
print("Part 1: " + str(count))

lines = []
count = 0
with open("../day03/input.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
        if len(lines) == 3:
            for i in range(0, len(lines[0])):
                testedLetter = lines[0][i]
                if lines[1].__contains__(testedLetter) & lines[2].__contains__(testedLetter):
                    count += get_letter_priority(testedLetter)
                    break
            lines = []
print("Part 2: " + str(count))
