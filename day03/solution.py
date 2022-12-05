def get_letter_priority(letter):
    if ord(letter) < 91:  # Majuscule
        return ord(letter) - 64 + 26  # +26 pour différencier des minuscules
    return ord(letter) - 96  # Minuscule


def part1():
    count = 0
    with open("../day03/input.txt", "r") as file:
        for line in file:
            line = line.strip()
            length: int = len(line) // 2
            for i in range(0, length):
                if line[i] in line[length:]:
                    count += get_letter_priority(line[i])
                    break
    return count


def part2():
    lines = []
    count = 0
    with open("../day03/input.txt", "r") as file:
        for line in file:
            lines.append(line.strip())
            if len(lines) == 3:
                for i in range(0, len(lines[0])):
                    tested_letter = lines[0][i]
                    if tested_letter in lines[1] and tested_letter in lines[2]:
                        count += get_letter_priority(tested_letter)
                        break
                lines = []
    return count
