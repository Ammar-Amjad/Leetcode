# Problem: 437. Path Sum III
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes). 

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:
The number of nodes in the tree is in the range [0, 1000].
- -109 <= Node.val <= 109
- -1000 <= targetSum <= 1000

## Approach: 
Code: [https://github.com/Ammar-Amjad/Leetcode/blob/main/Path%20Sum%20III/code.py](code.py)
The code implements a recursive approach to find the number of paths in a binary tree that sum up to a given target value. It uses a preorder traversal to visit each node in the tree.

The approach maintains a running sum (curr_sum) while traversing the tree. At each node, it checks if the current sum equals the target value (k) and increments the count if so. It also checks if the difference between the current sum and the target value exists in a hash map (h) and increments the count by the corresponding value.

The hash map h keeps track of the number of occurrences of each sum encountered so far. This allows the algorithm to consider all possible paths that sum up to the target value, even if they are not consecutive.

After processing a node and its children, the algorithm backtracks by decrementing the count for the current sum in the hash map.

Finally, the algorithm returns the total count of paths found.

## Complexity:  
Time complexity: O(N)
, where N is a number of nodes.
During preorder traversal, each node is visited once.

Space complexity: up to O(N)
to keep the hashmap
of prefix sums, where N is a number of nodes.