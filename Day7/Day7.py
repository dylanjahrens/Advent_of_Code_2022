from collections import defaultdict


def create_directories(input):

    terminal_output = []
    filepath = []
    sizes = defaultdict(int)

    with open(input, "r") as input_file:
        for line in input_file:
            terminal_output.append(line.strip())
    
    #parse input commands
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
            file_size, file_name = line.split()
            if file_size.isdigit():
                for i in range(len(filepath)):
                    #creating new dict entry with size as value
                    #and current filepath stack as key
                    sizes['/'.join(filepath[:i+1])] += int(file_size)

    return sizes


def part_1(dir):
    
    sum_under_max = 0
    MAX_SIZE = 100000

    for key, value in dir.items():
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

    for key, value in dir.items():
        if value > space_needed:
            delete_options.append(value)
    
    return print(min(delete_options))


if __name__ == "__main__":
    directory = create_directories('Day7_input.txt')
    part_1(directory)
    part_2(directory)
