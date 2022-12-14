from collections import defaultdict

def file_sizes(input):
    
    terminal_output = []
    filepath = []
    sizes = defaultdict(int)
    
    #PART1 VARIABLES AND CONSTANTS
    sum_under_max = 0
    MAX_SIZE = 100000

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


    #PART 2 VARIABLES AND CONSTANTS  
    total_space = 70000000
    update_size = 30000000
    used_space = sizes['/'] #value (size) of main directory
    free_space = total_space - used_space
    space_needed = update_size - free_space
    delete_options = []
    
    for key, value in sizes.items():
        #p1 to find directory size under max sums
        if value <= MAX_SIZE:
            sum_under_max += value
        #p2 to find eligible directories to delete
        if value > space_needed:
            delete_options.append(value)
    
    return print(sum_under_max, min(delete_options))


file_sizes('Day7_input.txt')