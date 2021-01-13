[graphs.png]
  1 ---- 2 ---- 3
  | \    |      |
  4  \   5 ---- 6
   \  \  |     /
    \  \ |    /
      -  7  -



1: [2, 4, 7]
2: [1, 3, 5]
3: [2, 6]
4: [7, 1]
5: [2, 6, 7]
6: [3, 5, 7]
7: [1, 4, 5, 6]


   1  2  3  4  5  6  7
1  0  1  0  1  0  0  1
2  1  0  1  0  1  0  0
3  0  1  0  0  0  1  0
4  1  0  0  0  0  0  1
5  0  1  0  0  0  1  1
6  0  0  1  0  1  0  1
7  1  0  0  1  1  1  0



{
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}

0 --- 1     2
|
3

COMPONENTS (0, 1, and 3) (2)


Bi-direction (1 <--> 2) There are possibly 1 directionals in graph
Un-directed (1 --- 2) Not possible to have 1 directionals in graph
Use adjacency matrix instead of adjacency list when dense
Weight: distance/time it takes to travel between two distances
We use a set to keep track of edges because it can't contain duplicates and its look-up is O(1)
Traversal vs Search: search stops when you find what you are looking for while traversal visits everything, but traversal is used in both circumstances


[graphs.png]
  1 ---- 2 ---- 3
  | \    |      |
  4  \   5 ---- 6
   \  \  |     /
    \  \ |    /
      -  7  -

Minimum spanning tree: efficiently going to the least amount of nodes

DEPTH FIRST TRAVERSAL
- Gives the shortest path to another specified node
- If there is more than one valid path, it will just find the first one

|     |
|     |
|     |
|  6  | +
|__2__| +  3

Visited: 

|     |
|     |
|  7  | +
|  5  | +
|__2__|  6

Visited: 3

|  1  | +
|  5  | +
|  4  | +
|  5  |
|__2__|  7

Visited: 3, 6

|  2  | +
|  4  | +
|  5  |
|  4  |
|  5  |
|__2__|  1

Visited: 3, 6, 7

|  7  | +
|  6  | +
|  5  |
|  3  |
|  2  |
|  4  |
|  5  |
|  4  |
|  5  |
|__2__|  5

Visited: 3, 6, 7, 1, 2

|  7  | -
|  6  | -
|  3  | -
|  2  | -
|  4  |
|  5  |
|  4  |
|  5  |
|__2__|  7 VISITED, NEXT... 6 VISITED, NEXT... 3 VISITED, NEXT... 4

Visited: 3, 6, 7, 1, 2, 5

|  7  | -
|  1  | -
|  4  | -
|  5  | -
|  4  | -
|  5  | -
|__2__| - 7 VISITED, NEXT... 1 VISITED, NEXT... 4 VISITED, NEXT...

Visited: 3, 6, 7, 1, 2, 5, 4


BREATH FIRST TRAVERSAL
- Gives the shortest path to all of the other nodes
- If there is more than one valid path, it will just find the first one

______________

             4
______________  

Visited: 

______________
[4, 1]  [4, 7]  
______________  [4]

Visited: 4

____________________________

[4, 1, 7]  [4, 1, 2]  [4, 7]  
____________________________  [4, 1]

Visited: 4, 1

_____________________________________________________

[4, 7, 1]  [4, 7, 6]  [4, 7, 5]  [4, 1, 7]  [4, 1, 2] 
_____________________________________________________  [4, 7]

Visited: 4, 1, 7

____________________________________________________________________________________

[4, 1, 2, 3]  [4, 1, 2, 5]  [4, 1, 2, 1]  [4, 7, 1]  [4, 7, 6]  [4, 7, 5]  [4, 1, 7]   
____________________________________________________________________________________  [4, 1, 2]

Visited: 4, 1, 7, 2

......
____________

[4, 1, 2, 3]  
____________  [4, 1, 2]

Visited: 4, 1, 7, 2