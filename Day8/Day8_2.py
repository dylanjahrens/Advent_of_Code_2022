def input_array(input):
    
    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        grid_list = [list(line.strip()) for line in file_lines]
        
    
    return grid_list

def scenic_score(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    high_score = 0

    for ri, row in enumerate(matrix):
        for ci, tree in enumerate(row):
            
            tree_value = int(tree)
            l_neighbors = 0
            r_neighbors = 0
            u_neighbors = 0
            d_neighbors = 0

            #if tree is on outside of grid its score will be 0
            if ri == 0 or ri == rows-1 or ci == 0 or ci == cols-1:
                continue

            else:
                #left
                for i in range(1, ci+1):
                    if tree_value > int(row[ci-i]):
                        l_neighbors +=1
                    else:
                        l_neighbors +=1
                        break
    
                #right
                for i in range(1, (cols-ci)):
                    if tree_value > int(row[ci + i]):
                        r_neighbors += 1
                    else:
                        r_neighbors += 1
                        break

                #up
                for i in range(1, ri+1):
                    if tree_value > int(matrix[ri - i][ci]):
                        u_neighbors +=1
                    else:
                        u_neighbors +=1
                        break

                #down
                for i in range(1, rows-ri):
                    if tree_value > int(matrix[ri + i][ci]):
                        d_neighbors +=1
                    else:
                        d_neighbors +=1
                        break
            
            score = l_neighbors * r_neighbors * u_neighbors * d_neighbors

            if score > high_score:
                high_score = score

    return print(high_score)

inp_matrix = input_array('Day8_input.txt')
scenic_score(inp_matrix)