class Directory:
    def __init__(self, name):
        self.name = name
        self.storage = 0
        self.files = []

    def add_storage(self, file):
        file = file.split(" ")
        if file[1] not in self.files:
            self.files.append(file[1])
            self.storage += int(file[0])

    def __eq__(self, other):
        return str(self.name) == str(other.name)


def make_directory_array():
    current_dir = []
    tree = []
    with open('../day07/input.txt') as f:
        for line in f:
            line = line.strip()
            if "$ cd .." in line:
                current_dir.pop()
            elif "$ cd" in line:
                current_dir.append(line[5:])  # "$ cd dir" -> "dir"
                directory = Directory(".".join(current_dir))
                if directory not in tree:
                    tree.append(directory)
            elif any(char.isdigit() for char in line):  # if line contains a digit
                directory = Directory(".".join(current_dir))
                if directory not in tree:
                    tree.append(directory)
                tree[tree.index(directory)].add_storage(line)
    copy_array = tree.copy()
    for directory in tree:
        for sub_dir in copy_array:
            if directory.name in sub_dir.name and directory.name != sub_dir.name:
                directory.storage += sub_dir.storage
    return tree


def part1():
    array = make_directory_array()
    count = 0
    for any_dir in array:
        if any_dir.storage <= 100000:
            count += any_dir.storage
    return count


def part2():
    array = make_directory_array()
    temp_min = array[0].storage
    space_needed = 30000000 - (70000000 - temp_min)
    for directory in array:
        if directory.storage >= space_needed:
            if directory.storage < temp_min:
                temp_min = directory.storage
    return temp_min
