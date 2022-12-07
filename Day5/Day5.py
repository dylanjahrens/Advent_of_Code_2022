def cargo():

    with open('Day5_input.txt', "r") as input_file:
        instructions = input_file.readlines()[10:]
        instruction_list = [line.strip().split(' ') for line in instructions]

    cargo_grid = [
        [['F'],['T'],['C'],['L'],['R'],['P'],['G'],['Q']],
        [['N'],['W'],['H'],['W'],['R'],['F'],['S'],['J']],
        [['F'],['B'],['H'],['W'],['P'],['M'],['Q']],
        [['V'],['S'],['T'],['D'],['F']],
        [['Q'],['L'],['D'],['W'],['V'],['F'],['Z']],
        [['Z'],['C'],['L'],['S']],
        [['Z'],['B'],['M'],['V'],['D'],['F']],
        [['T'],['J'],['B']],
        [['Q'],['N'],['B'],['G'],['L'],['S'],['P'],['H']],
    ]

    for line in instruction_list:
        quantity = int(line[1])
        start = int(line[3]) -1
        end = int(line[5]) -1
        for i in range(quantity):
            value = cargo_grid[start].pop()
            cargo_grid[end].append(value)
    
    end_values = ''
    for line in cargo_grid:
        for item in line[-1]:
            end_values += item

    return print(end_values)
        
cargo()