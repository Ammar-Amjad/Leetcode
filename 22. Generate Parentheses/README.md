# Problem: 22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8

## Approach: 

Code: [https://github.com/Ammar-Amjad/Leetcode/blob/main/Generate%20Parentheses/code.py](code.py)
The code implements a recursive depth-first search (DFS) algorithm to generate all valid combinations of parentheses. It takes an integer n as input and returns a list of strings representing the valid combinations.

The dfs function performs the DFS traversal. It adds an opening parenthesis if the count of openings is less than n and recursively calls itself. It adds a closing parenthesis if the count of closings is less than the count of openings and recursively calls itself. The base case is when the length of the string equals 2 * n, indicating a valid combination.

The generateParenthesis function initializes an empty list to store the combinations. It calls the dfs function to start the DFS traversal. Finally, it returns the list of valid combinations.

To use the code, create an instance of the Solution class and call the generateParenthesis method with the desired value of n.

## Complexity: 
Time Complexity: O(4^n/sqrt(n))
Space Complexity: O(4^n/sqrt(n))