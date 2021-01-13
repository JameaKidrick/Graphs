# from projects.graph.util import Queue
# from projects.graph.graph import Graph

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    '''
    given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.
    # '''
    children = [child for parent, child in ancestors]
    print(children)
    if starting_node not in children:
        return -1
    # CREATE A QUEUE
    qq = Queue()
    # ENQUEUE STARTING VERTEX
    qq.enqueue([starting_node])
    all_paths = []
    # CREATE A SET OF TRAVERSED VERTICES
    visited = set()
    # WHILE QUEUE IS NOT EMPTY:
    while qq.size() > 0:
        # DEQUEUE THE FIRST VERTEX
        path = qq.dequeue()
        # IF NOT VISITED:
        if path[-1] not in visited:
            # DO THE THING
            # ADD IT TO VISITED
            visited.add(path[-1])
            # ENQUEUE ALL NEIGHBORS
            for child in ancestors:
                if child[1] == path[-1]:
                    new_path = list(path)
                    new_path.append(child[0])
                    qq.enqueue(new_path)
        all_paths.append(path)
    longest = all_paths[0]
    for each_path in all_paths:
        if len(each_path) > len(longest):
            longest = each_path
    print(longest[len(longest) - 1])
    return longest[len(longest) - 1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

'''

LOGIC 👇👇👇

_____________

            6
_____________  

Visited: 

______________
[6, 3]  [6, 5]  
______________  [6]

Visited: 6

______________
[6, 3]  [6, 5]  
______________  [6, 5]

Visited: 6, 5

______________
[6, 5, 4]  [6, 3]  
______________  [6, 5]

Visited: 6, 5

______________
[6, 3, 1]  [6, 3, 2]  [6, 5, 4]   
______________  [6, 3]

Visited: 6, 5, 3

______________
[6, 3, 1]  [6, 3, 2]     
______________  [6, 5, 4]

Visited: 6, 5, 3, 4

Ancestry: [6, 5, 4]

______________
[6, 3, 1]       
______________  [6, 3, 2]

Visited: 6, 5, 3, 4, 2

Ancestry: [6, 5, 4], [6, 3, 2]

______________
[6, 3, 1, 10]
______________  [6, 3, 1]

Visited: 6, 5, 3, 4, 1

Ancestry: [6, 5, 4], [6, 3, 2]

______________

______________  [6, 3, 1, 10]

Visited: 6, 5, 3, 4, 1, 10

Ancestry: [6, 5, 4], [6, 3, 2], [6, 3, 1, 10]

______________

______________ 

Visited: 6, 5, 3, 4, 1, 10

Ancestry: [6, 5, 4], [6, 3, 2], [6, 3, 1, 10]

Compare ancestry inner array lengths; Largest length array's last element = answer (10)

'''