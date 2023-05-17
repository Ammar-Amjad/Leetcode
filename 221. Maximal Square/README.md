# Problem: 22. Generate Parentheses
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area. 

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
 
Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is '0' or '1'.

## Approach: 

Code: [https://github.com/Ammar-Amjad/Leetcode/blob/main/Generate%20Parentheses/code.py](code.py)
The given code implements the maximalSquare function, which finds the maximum square of '1's in a given matrix.

The approach is to use dynamic programming to build a 2D table (dp) that represents the maximum square size at each position in the matrix. The dp table is initialized with zeros.

For each cell in the matrix, if the value is '1', the corresponding dp cell is updated by taking the minimum value from the adjacent cells (above, left, and diagonally above-left) and adding 1. This represents the largest square that can be formed with the current cell as the bottom-right corner.

Simultaneously, the maximum side length (max_side) is updated with the largest value in the dp table.

Finally, the area of the largest square is computed by multiplying max_side by itself and returned as the result.

## Complexity: 
Time complexity : O(mn).
Single pass - row x col (m=row; n=col)

Space complexity : O(mn). 
Additional space for dp grid (don't need to worry about additional 1 row and col).