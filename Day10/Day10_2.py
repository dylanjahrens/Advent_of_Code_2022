#global variables
x = 1
cycle = 0
signal_strength = 0
matrix = [[' ' for _ in range(40)] for _ in range(6)]


def parse(file):
    with open(file, "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip() for line in file_lines]

    return input_list


def new_cycle():
    
    global cycle
    global x
    global signal_strength
    cycle_list = [20, 60, 100, 140, 180, 220]

    cycle +=1

    if cycle in cycle_list:
        signal_strength += (cycle * x)

    pixel_row = (cycle-1) // 40 #-1 for matrix indexing
    pixel_col = (cycle-1) % 40
    sprite = [(x-1)%40, (x)%40, (x+1)%40]

    for i in range(3):
        if sprite[i] == pixel_col:
            matrix[pixel_row][pixel_col] = '#'


def execute(inp):

    global x
    global cycle

    for instruction in inp:
        new_cycle()

        if instruction.startswith('addx'):
            new_cycle()
            v = int(instruction.split()[-1])
            x += v

    #part1
    print(f'Signal Strength: {signal_strength}')
    print()

    #part2
    for line in matrix:
        print(''.join(line))


if __name__ == "__main__":
    input_directions = parse('Day10_input.txt')
    execute(input_directions)


        




