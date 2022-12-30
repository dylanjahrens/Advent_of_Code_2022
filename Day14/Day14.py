def get_rocks(input):

    data = open(input).read().strip()
    coord_list = []
    for line in data.split('\n'):
        points = [tuple(map(int, p.split(','))) for p in line.split(' -> ')]
        coord_list.append(points)

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
    
    bottom = max((y for x, y in rocks))

    offsets = {
        "down": (0, 1),
        "diag_l": (-1, 1),
        "diag_r": (1, 1),
    }
    grains = set()
    
    while True: #while ALL sand is still falling before endless void
        
        grain_pos = (500,0) #new grain
        attempts = 0

        while attempts < 3: # while grain can still move

            #try 3 potential positions
            for y_offset, x_offset in offsets.values():
                potential_pos = (grain_pos[0] + y_offset, grain_pos[1] + x_offset)
                if potential_pos not in rocks and potential_pos not in grains:
                    grain_pos = potential_pos
                    attempts = 0
                    if grain_pos[1] >= bottom:
                        return print(len(grains))
                    break
                else:
                    attempts += 1
                    
        grains.add(grain_pos) #if grain can no longer move
        

rock_list = get_rocks('input.txt')
move_sand(rock_list)

