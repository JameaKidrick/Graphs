# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

# islands consist of - connected components
# connected - neighbors (edges)
# directions, nsew - edges
# 2d array - graph
# returns (shape of solution) - number of islands

# How could we write a get neighbor function that uses this shape?
# Offset coordinates

# How can we find the extent of an island?
# Either of our traversals to find all of the nodes in an island

# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1

# INSTRUCTOR SOLUTION

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
        

def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    if y > 0 and matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    return neighbors
    

def dfs(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        v = s.pop()
        if not visited[v[1]][v[0]]:
            visited[v[1]][v[0]] = True
            for neighbor in get_neighbors(v[0], v[1], matrix):
                s.push(neighbor)
    return visited
    

def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dfs(x, y, matrix, visited)
                    island_count += 1
                else:
                    visited[y][x] = True
    return island_count
    
def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))
        

matrix = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
print_matrix(matrix)
island_counter(matrix)
Collapse


# STUDENT SOLUTION

def get_neighbors(matrix, node_x, node_y, size):
    neighbors = []
    if node_y > 0:
        n_neighbor = (node_y-1, node_x)
        neighbors.append(n_neighbor)
    if node_x > 0:
        w_neighbor = (node_y, node_x-1)
        neighbors.append(w_neighbor)
    if node_y < size-1:
        s_neighbor = (node_y+1, node_x)
        neighbors.append(s_neighbor)
    if node_x < size-1:
        e_neighbor = (node_y, node_x+1)
        neighbors.append(e_neighbor)
    return neighbors
    
def dft_traversal_recursive(matrix, node_x, node_y, size, visited):
    neighbors = get_neighbors(matrix, node_x, node_y, size)
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.add(neighbor)
            neighbor_x = neighbor[0]
            neighbor_y = neighbor[1]
            if matrix[neighbor_x][neighbor_y] == 1:
                dft_traversal_recursive(matrix, neighbor_x, neighbor_y,
                                        size, visited)
def find_islands(matrix):
    size = len(matrix)
    visited = set()
    islands = 0
    for i in range(size):
        for j in range(size):
            if (i, j) not in visited:
                visited.add((i, j))
                if matrix[i, j] == 1:
                    dft_traversal_recursive(matrix, j, i, size, visited)
                    islands += 1
    return islands


# STUDENT SOLUTION 2

def island_counter(islands):
    num_islands = 0
    # iterate through the islands
    for y in range(0, len(islands)):
        for x in range(0, len(islands[y])):
            # if the island-node is part of an island and hasn't been visited
            if islands[y][x] == 1:
                # you've found an island, so increment
                num_islands += 1
                # BFT through the island-node's neighbors
                islands = visit_neighbors(x, y, islands)
    return num_islands

def visit_neighbors(x, y, islands):
    # NORTH
    if y > 0:  # if not at northern edge
        # and neighbor is an island-node
        if islands[y-1][x] == 1:
            # mark it visited by updating value to 0
            islands[y-1][x] = 0
            # and visit all it's neighbors
            islands = visit_neighbors(x, y-1, islands)
            
    # SOUTH
    if y < 4:
        if islands[y+1][x] == 1:
            islands[y+1][x] = 0
            islands = visit_neighbors(x, y+1, islands)
            
    # EAST
    if x < 4:
        if islands[y][x+1] == 1:
            islands[y][x+1] = 0
            islands = visit_neighbors(x+1, y, islands)
            
    # WEST
    if x > 0:
        if islands[y][x-1] == 1:
            islands[y][x-1] = 0
            islands = visit_neighbors(x-1, y, islands)
            
    return islands
    

result = island_counter(islands)

print(result)