class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None:
            return grid
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        delete = set()
        visited = set() 
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    queue.append((i, j, 0))         
                elif grid[i][j] == 1:
                    delete.add((i, j))
        
        
        
        time = 0
        
        while queue:
            i, j, time = queue.popleft() 
            
            if (i, j) in delete:
                delete.remove((i, j))
            
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newi = i + x
                newj = j + y 
                if 0 <= newi < rows and 0 <= newj < cols and grid[newi][newj] == 1 and (newi, newj) not in visited:
                    visited.add((newi, newj))
                    queue.append((newi, newj, time + 1))
         
        return time if delete == set() else -1
            
        