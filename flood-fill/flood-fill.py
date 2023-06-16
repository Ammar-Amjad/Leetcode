class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # DFS
        orig_color = grid[sr][sc]
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visited = set()
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == orig_color and (i, j) not in visited:
                grid[i][j] = color
                visited.add((i, j))
                
                for x, y in directions:
                    dfs(i + x, j + y)            
                
            else:
                return 0                            
        
        dfs(sr, sc)
        return grid
        
        
        
        
        
#         # BFS
#         stack = [(sr, sc)]
#         directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
#         orig_color = grid[sr][sc]
        
#         if orig_color == color:
#             return grid
        
#         while stack: 
#             sr, sc = stack.pop()
#             grid[sr][sc] = color
#             for i, j in directions:
#                 sri = sr + i
#                 scj = sc + j
#                 if 0 <= sri < len(grid) and 0 <= scj < len(grid[0]) and (sri, scj) not in stack:
#                     if grid[sri][scj] == orig_color:
#                         stack.append((sri,scj))
#         return grid
        
        
        