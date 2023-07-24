class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int: 
        self.dp = {}
        
        def dfs(i, j):
            
            if (i, j) in self.dp:
                return self.dp[(i, j)]
            
            if i == len(t1) or j == len(t2):
                return 0
            
            if t1[i] == t2[j]:
                self.dp[(i, j)] = 1 + dfs(i + 1, j + 1)
                return self.dp[(i, j)]
            
            self.dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return self.dp[(i, j)]
        
        return dfs(0, 0)