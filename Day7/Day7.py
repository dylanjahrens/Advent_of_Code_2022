from collections import defaultdict


def create_directories(input):

    filepath = []
    sizes = defaultdict(int)

    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        terminal_output = [line.strip() for line in file_lines]
    
    for line in terminal_output:
        if line.startswith('$ cd'):
            directory = line.split()[-1]
            if directory == '..':
                filepath.pop()
            else:
                filepath.append(directory)

        elif line.startswith('$ ls'):
            continue

        else:
            file_size = line.split()[0]
            if file_size.isdigit():
                for i in range(len(filepath)):
                    sizes['/'.join(filepath[:i+1])] += int(file_size)

    return sizes


def part_1(dir):
    
    sum_under_max = 0
    MAX_SIZE = 100000

    for value in dir.values():
        if value <= MAX_SIZE:
            sum_under_max += value

    return print(sum_under_max)


def part_2(dir):
    
    TOTAL_SPACE = 70000000
    UPDATE_SIZE = 30000000
    used_space = dir['/'] #value (size) of main directory
    free_space = TOTAL_SPACE - used_space
    space_needed = UPDATE_SIZE - free_space
    delete_options = []

    for value in dir.values():
        if value > space_needed:
            delete_options.append(value)
    
    return print(min(delete_options))


if __name__ == "__main__":
    directory = create_directories('Day7_input.txt')
    part_1(directory)
    part_2(directory)
