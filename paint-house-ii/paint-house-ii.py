class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        rows = len(costs)
        cols = len(costs[0])
        
        @cache
        def dfs(i, c):
            if i == rows - 1:
                return costs[i][c]
            
            colorsList = [float('inf')]
            for color in range(cols):
                if color != c:
                    colorsList += [dfs(i + 1, color)]
            
            return costs[i][c] + min(colorsList)            
            
        
        total = [float('inf')]
        for c in range(cols):
            total += [dfs(0, c)]
            
        return min(total)