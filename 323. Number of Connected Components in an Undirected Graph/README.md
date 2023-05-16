# Problem: 323. Number of Connected Components in an Undirected Graph
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph. 

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 
Constraints:
- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges.

## Approach:
The given code implements the union-find algorithm to count the number of connected components in a graph. It uses the concepts of parent array (par) and rank to efficiently perform union and find operations. Initially, each node is considered as a separate component with its parent as itself and rank as 1. The find function performs path compression by updating the parent of each node during the find operation. The union function merges two components by comparing their ranks and updating the parent accordingly. By iterating through the edges and performing unions, the code determines the number of unique components. The time complexity is O(E * α(E)), where E is the number of edges and α(E) is the inverse Ackermann function. The space complexity is O(V), where V is the number of nodes.

## Code: [link to the code file](code.py)

## Complexity: time and space complexity
The time complexity of the given code is O(E * α(E)), 
where E is the number of edges in the graph and α(E) is the inverse Ackermann function. The inverse Ackermann function grows very slowly and can be considered a constant factor for practical purposes. Therefore, the time complexity can be simplified to O(E).

The space complexity of the code is O(V), 
where V is the number of nodes in the graph. The space is primarily used to store the parent array (par) and the rank array, both of which have a length equal to the number of nodes. Therefore, the space complexity is linear in terms of the number of nodes.