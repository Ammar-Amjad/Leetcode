# Problem: 91. Decode Ways
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

## Approach: 
The code implements a recursive depth-first search (DFS) algorithm to generate all valid combinations of parentheses. It takes an integer n as input and returns a list of strings representing the valid combinations.

The dfs function performs the DFS traversal. It adds an opening parenthesis if the count of openings is less than n and recursively calls itself. It adds a closing parenthesis if the count of closings is less than the count of openings and recursively calls itself. The base case is when the length of the string equals 2 * n, indicating a valid combination.

The generateParenthesis function initializes an empty list to store the combinations. It calls the dfs function to start the DFS traversal. Finally, it returns the list of valid combinations.

To use the code, create an instance of the Solution class and call the generateParenthesis method with the desired value of n.

## Complexity: 
Time Complexity: O(4^n/sqrt(n))
Space Complexity: O(4^n/sqrt(n))