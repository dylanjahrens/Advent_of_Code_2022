def input_array(input):
    
    with open(input, "r") as input_file:
        file_lines = input_file.readlines()
        grid_list = [list(line.strip()) for line in file_lines]
        
    
    return grid_list

def visible_trees(matrix):

    row_count = len(matrix)
    col_count = len(matrix[0])
    trees_visible = 0

    for ri, row in enumerate(matrix):
        for ci, tree in enumerate(row):
            tree_value = int(tree)
            #if tree is on outside of grid count it
            if ri == 0 or ri == row_count-1 or ci == 0 or ci == col_count-1:
                trees_visible +=1
            #else check sizes of all trees on all sides 
            else:
                l_competetors = set()
                r_competetors = set()
                u_competetors = set()
                d_competetors = set()
                #left
                for l in range(ci):
                    l_competetors.add(int(row[l]))
                #right
                for r in range(ci+1, col_count):
                    r_competetors.add(int(row[r]))
                #up
                for u in range(ri):
                    u_competetors.add(int(matrix[u][ci]))
                #down
                for d in range(ri+1, col_count):
                    d_competetors.add(int(matrix[d][ci]))
                
                if (tree_value > max(l_competetors) or tree_value > max(r_competetors) or
                tree_value > max(u_competetors) or tree_value > max(d_competetors)):
                    trees_visible +=1

    print(trees_visible)


inp_matrix = input_array('Day8_input.txt')
visible_trees(inp_matrix)
