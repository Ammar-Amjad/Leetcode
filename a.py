import os

topics = [
    "Array", "String", "Linked List", "Stack", "Queue", "Binary Tree",
    "Binary Search Tree", "Heap", "Graph", "Dynamic Programming", "Backtracking",
    "Greedy Algorithms", "Sorting and Searching", "Hashing", "Bit Manipulation",
    "Recursion", "Divide and Conquer", "Math", "Two Pointers", "Sliding Window",
    "Trie", "Union Find (Disjoint Set)", "Topological Sorting", "Segment Tree",
    "Binary Indexed Tree (Fenwick Tree)", "Depth-First Search (DFS)",
    "Breadth-First Search (BFS)", "Memoization", "Geometry",
    "Operating System Concepts (e.g., process scheduling, memory management)"
]

# Directory where you want to create the folders
base_directory = "/path/to/your/repository/"

for topic in topics:
    directory = os.path.join(base_directory, topic)
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")
