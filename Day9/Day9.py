from collections import OrderedDict

def simulate_rope(input, number_of_knots):

    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        directions = [line.strip().split() for line in file_lines]

    #DIRECTIONAL CHECKERS
    #up right down left
    d = ['U','R','D','L']
    #1 step URDL directions
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    #surrounding (1 step away)
    touching_r = [0,1,1,1,0,-1,-1,-1]
    touching_c = [-1,-1,0,1,1,1,0,-1]
    #2 steps away
    two_steps = ['U','R','D','L','UR','UR','UR','DR','DR','DR','DL','DL','DL','UL','UL','UL']
    two_steps_r = [-2,0,2,0,-2,-1,-2,1,2,2,2,1,2,-1,-2,-2]
    two_steps_c = [0,2,0,-2,1,2,2,2,1,2,-1,-2,-2,-2,-1,-2]

    #STARTING POSITIONS
    #ordered dict where the key is the knot # (0 is head) and value is [r,c] position
    #knots[0][0] gives row number of knot 0
    #knots[0][1] gives col number of knot 0
    knots = OrderedDict()
    for i in range(number_of_knots):
        knots[i] = [0, 0]

    #set of unique tail positions
    tail_positions = {(0,0)}

    for line in directions:
        dir, steps = line[0], int(line[1])
        d_index = d.index(dir)

        for s in range(steps):
            #for each step the H (knot 0) moves in that direction
            knots[0][0] += dr[d_index]
            knots[0][1] += dc[d_index]
            
            #then check each subsequent knot to see if it needs to move
            for i in range(1,number_of_knots):
                head = i-1
                tail = i

                #if T is overlapped with H, don't move
                if knots[head] == knots[tail]:
                    continue
                
                #if T is touching H, don't move
                for i in range(8):
                    row = knots[tail][0] + touching_r[i]
                    col = knots[tail][1] + touching_c[i]
                    if knots[head] == [row, col]:
                        continue
                
                #if H is 2 steps away, move either URDL or diagonally to touch
                for i in range(len(two_steps)):
                    row = knots[tail][0] + two_steps_r[i]
                    col = knots[tail][1] + two_steps_c[i]
                    if knots[head] == [row, col]:
                        for l in two_steps[i]:
                            diag_index = d.index(l)
                            knots[tail][0] += dr[diag_index]
                            knots[tail][1] += dc[diag_index]
                
            tail_positions.add((knots[number_of_knots-1][0], knots[number_of_knots-1][1]))

    return print(len(tail_positions))

#for part 1 number of knots = 2 (H and T), part 2 = 10
simulate_rope('Day9_input.txt', 10)