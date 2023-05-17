# Problem: 48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation. 

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

## Approach: 

Code: [https://github.com/Ammar-Amjad/Leetcode/tree/main/48.%20Rotate%20Image/code.py](code.py)
The provided code implements a solution to rotate a square matrix in-place by 90 degrees clockwise. The approach involves two steps: transposing the matrix by swapping elements across its diagonal, and then reversing each row horizontally. These operations effectively rotate the matrix 90 degrees clockwise. The code defines two separate functions, "transpose_matrix" and "reverse," which are then called within the "rotate" method of the "Solution" class. The "rotate" method takes a matrix as input and modifies it in-place.

## Complexity: 
Let M be the number of cells in the grid.

Time complexity : O(M). 
We perform two steps; transposing the matrix, and then reversing each row. Transposing the matrix has a cost of O(M) because we're moving the value of each cell once. Reversing each row also has a cost of O(M), because again we're moving the value of each cell once.

Space complexity : O(1) because we do not use any other additional data structures.