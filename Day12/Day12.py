from heapq import heappush, heappop

with open('Day12_input.txt', "r") as input_file:
    file_lines = input_file.readlines()
    maze = [list(line.strip()) for line in file_lines]

all_starts = []
route_lengths = []

for y, row in enumerate(maze):
    for x, col in enumerate(row):
        if col == "S":
            start = [(y, x)]
            maze[y][x] = 1
        elif col == "E":
            end = (y,x)
            maze[y][x] = 26
        else:
            maze[y][x] = ord(col) - 96
        if maze[y][x] == 1:
            all_starts.append((y,x))

offsets = {
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
        "left": (0, -1)
    }

rows = len(maze)
cols = len(maze[0])

def get_neighbors(position):
    neighbors = []
    for row_offset, col_offset in offsets.values():
        neighbor = (position[0] + row_offset, position[1] + col_offset)
        if (0<=neighbor[0]<rows and 0<=neighbor[1]<cols
            and maze[neighbor[0]][neighbor[1]] <= maze[position[0]][position[1]]+1):
            neighbors.append(neighbor)

    return neighbors 


def get_steps(starting_pos):
    
    heap = []
    for s in starting_pos:
        visited = set(s)
        heappush(heap, (0, s))

        while True:
            if not heap:
                break

            steps, node = heappop(heap) #lowest item in heap
            if node not in visited:
                visited.add(node)
                if node == end:
                    route_lengths.append(steps)
                    break
                for rnew, cnew in get_neighbors(node):
                    heappush(heap, (steps+1, (rnew, cnew)))
    
    return print(min(route_lengths))

get_steps(start)
get_steps(all_starts)
