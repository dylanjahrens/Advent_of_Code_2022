def get_rocks(input):
    
    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        input_list = [line.strip().split() for line in file_lines]

    coord_list = []
    for path in input_list:
        path_coords = []
        for co in path:
            if co != '->':
                x,y = co.split(',')
                path_coords.append((int(x), int(y)))
        coord_list.append(path_coords)

    rocks = set()
    for path in coord_list:
        for i in range(len(path)-1):
            x,y = path[i][0], path[i][1]
            x2,y2 = path[i+1][0], path[i+1][1]

            if x == x2:
                if y < y2:
                    for i in range(y, y2+1):
                        rocks.add((x,i))
                else:
                    for i in range(y2, y+1):
                        rocks.add((x,i))
            elif y == y2:
                if x < x2:
                    for i in range(x, x2+1):
                        rocks.add((i,y))
                else:
                    for i in range(x2, x+1):
                        rocks.add((i,y))

    return rocks
    

def move_sand(rocks):
    
    bottom = 0 
    for rock in rocks:
        if rock[1] > bottom:
            bottom = rock[1]
    bottom += 2

    offsets = {
        "down": (0, 1),
        "diag_l": (-1, 1),
        "diag_r": (1, 1),
    }
    grains = set()
    
    while True:
        
        grain_pos = (500,0)
        attempts = 0

        while attempts < 3:

            for y_offset, x_offset in offsets.values():
                potential_pos = (grain_pos[0] + y_offset, grain_pos[1] + x_offset)
                if (potential_pos not in rocks and
                    potential_pos not in grains and
                    potential_pos[1] < bottom):
                    grain_pos = potential_pos
                    attempts = 0
                    break
                else:
                    attempts += 1       

        grains.add(grain_pos)
        
        if grain_pos == (500,0):
            return print(len(grains))
        

rock_list = get_rocks('input.txt')
move_sand(rock_list)
