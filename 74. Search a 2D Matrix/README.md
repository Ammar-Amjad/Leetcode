# Problem: 74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

## Approach: 
The given code implements a binary search algorithm to search for a target value in a 2D matrix. The matrix is represented as a list of lists, where each inner list represents a row of the matrix. The approach treats the 2D matrix as a 1D array by calculating its total length as m * n. It initializes two pointers, L and R, representing the start and end indices of the search range. It performs a binary search by calculating the middle index M and converting it back to row and column indices. It compares the value at the middle index with the target and adjusts the search range accordingly. The process continues until the target is found or the search range is exhausted. Finally, it returns True if the target is found and False otherwise.

## Complexity: 
The time complexity of the provided binary search algorithm is O(log(m * n)), where m and n are the dimensions of the matrix. This is because the algorithm performs a binary search on a 1D array of size m * n. In each iteration, the search range is halved, resulting in a logarithmic time complexity.

The space complexity of the algorithm is O(1) since it uses a constant amount of additional space. The variables used for storing indices (m, n, L, R, M, ri, ci) require a constant amount of space, regardless of the size of the input matrix. Therefore, the space complexity is constant or O(1).