class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        islands = 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        rLen = len(grid)
        cLen = len(grid[0])

        for i in range(rLen):
            for j in range(cLen):
                if grid[i][j] == '1':
                    islands += 1
                    queue.append((i, j))
                    grid[i][j] = '0'
                while queue:
                    r, c = queue.popleft()
                    
                    for x, y in directions:
                        if 0 <= x + r < rLen and 0 <= y + c < cLen and grid[x + r][y +c] == '1':
                            queue.append((x + r, y + c))
                            grid[x + r][y + c] = '0'
        
        return islands
