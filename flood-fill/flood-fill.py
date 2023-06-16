class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS
        stack = [(sr, sc)]
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        orig_color = grid[sr][sc]
        if orig_color == color:
            return grid
        
        while stack: 
            print(stack)
            sr, sc = stack.pop()
            grid[sr][sc] = color
            for i, j in directions:
                sri = sr + i
                scj = sc + j
                if 0 <= sri < len(grid) and 0 <= scj < len(grid[0]) and (sri, scj) not in stack:
                    if grid[sri][scj] == orig_color:
                        stack.append((sri,scj))
        return grid
        
        # DFS
        