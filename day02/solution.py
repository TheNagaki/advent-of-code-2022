eq = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def lose(move1):
    return eq[move1] - 1 if eq[move1] > 1 else 3


def draw(move1):
    return 3 + eq[move1]


def win(move1):
    return 6 + (eq[move1] + 1 if eq[move1] < 3 else 1)


def calc_score(move1, move2):
    s1 = eq[move1]
    s2 = eq[move2]
    if s1 == s2:  # Cas d'égalité
        return draw(move1)
    if s2 == s1 + 1 or s2 == s1 - 2:  # Cas A-Y, B-Z ou C-X
        return win(move1)
    return lose(move1)  # Cas A-Z, B-X ou C-Y


def calc_score2(move1, move2):
    switcher = {
        "X": lose(move1),
        "Y": draw(move1),
        "Z": win(move1)
    }
    return switcher.get(move2)


def part2():
    with open("../day02/input.txt", "r") as f:
        score = 0
        for line in f:
            score += calc_score2(line[0], line[2])
    f.close()
    return score


def part1():
    with open("../day02/input.txt", "r") as f:
        score = 0
        for line in f:
            score += calc_score(line[0], line[2])
    f.close()
    return score
