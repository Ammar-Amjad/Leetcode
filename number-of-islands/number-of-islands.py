class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == '0':
                return 0

            grid[i][j] = '0'
            
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            
            return 0 
        
        count = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    count += 1
                    dfs(x, y)
                
        return count
        