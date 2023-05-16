# Problem: 1197. Minimum Knight Moves
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists. 

Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:
Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 
Constraints:
- -300 <= x, y <= 300
- 0 <= |x| + |y| <= 300

## Approach:
The minKnightMoves function uses dynamic programming and recursion to find the minimum number of moves required for a knight to reach the target position (x, y) on a chessboard. It employs memoization with the lru_cache decorator to store previously calculated results. The base cases are when the knight is already at the target (x + y = 0) or one move away from the target (x + y = 2). Otherwise, it recursively calculates the minimum moves by considering two possible knight moves and choosing the minimum. The final result is returned as the minimum number of moves required.

## Code: [link to the code file](code.py)

## Complexity: time and space complexity

the time complexity can be considered as O(x * y).
The time complexity of the code depends on the number of recursive calls made and the time it takes to compute each call. Since the lru_cache decorator eliminates redundant recursive calls by memoizing the results, the number of unique recursive calls is limited.

The space complexity of the given code is O(x * y),
where x and y are the absolute values of the target coordinates. This is because the lru_cache decorator stores previously calculated results in a cache, which can potentially hold x * y unique positions.
