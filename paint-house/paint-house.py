class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        @cache
        def dfs(i, c):
            if i == len(costs) - 1:
                return costs[i][c]
            
            colorsList = [float('inf')]
            for color in range(len(costs[0])):
                if color != c:
                    colorsList += [dfs(i + 1, color)]
            
            return costs[i][c] + min(colorsList)            
            
        
        total = [float('inf')]
        for c in range(len(costs[0])):
            total += [dfs(0, c)]
            
        return min(total)